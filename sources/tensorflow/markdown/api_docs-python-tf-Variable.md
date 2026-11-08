[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/Variable)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/Variable?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2FVariable%3Fversion%3Dstable&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#args_1)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#raises_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#attributes_1)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#child_classes_2)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#methods_2)
    *   [assign](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#assign)
        
    *   [assign\_add](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#assign_add)
        
    *   [assign\_sub](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#assign_sub)
        
    *   [batch\_scatter\_update](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#batch_scatter_update)
        
    *   [count\_up\_to](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#count_up_to)
        
    *   [eval](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#eval)
        
    *   [experimental\_ref](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#experimental_ref)
        
    *   [from\_proto](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#from_proto)
        
    *   [gather\_nd](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#gather_nd)
        
    *   [get\_shape](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#get_shape)
        
    *   [initialized\_value](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#initialized_value)
        
    *   [load](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#load)
        
    *   [read\_value](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#read_value)
        
    *   [ref](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#ref)
        
    *   [scatter\_add](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#scatter_add)
        
    *   [scatter\_div](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#scatter_div)
        
    *   [scatter\_max](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#scatter_max)
        
    *   [scatter\_min](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#scatter_min)
        
    *   [scatter\_mul](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#scatter_mul)
        
    *   [scatter\_nd\_add](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#scatter_nd_add)
        
    *   [scatter\_nd\_sub](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#scatter_nd_sub)
        
    *   [scatter\_nd\_update](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#scatter_nd_update)
        
    *   [scatter\_sub](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#scatter_sub)
        
    *   [scatter\_update](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#scatter_update)
        
    *   [set\_shape](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#set_shape)
        
    *   [sparse\_read](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#sparse_read)
        
    *   [to\_proto](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#to_proto)
        
    *   [value](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#value)
        
    *   [\_\_abs\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__abs__)
        
    *   [\_\_add\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__add__)
        
    *   [\_\_and\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__and__)
        
    *   [\_\_div\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__div__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__eq__)
        
    *   [\_\_floordiv\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__floordiv__)
        
    *   [\_\_ge\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__ge__)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__getitem__)
        
    *   [\_\_gt\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__gt__)
        
    *   [\_\_invert\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__invert__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__iter__)
        
    *   [\_\_le\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__le__)
        
    *   [\_\_lt\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__lt__)
        
    *   [\_\_matmul\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__matmul__)
        
    *   [\_\_mod\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__mod__)
        
    *   [\_\_mul\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__mul__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__ne__)
        
    *   [\_\_neg\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__neg__)
        
    *   [\_\_or\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__or__)
        
    *   [\_\_pow\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__pow__)
        
    *   [\_\_radd\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__radd__)
        
    *   [\_\_rand\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__rand__)
        
    *   [\_\_rdiv\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__rdiv__)
        
    *   [\_\_rfloordiv\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__rfloordiv__)
        
    *   [\_\_rmatmul\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__rmatmul__)
        
    *   [\_\_rmod\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__rmod__)
        
    *   [\_\_rmul\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__rmul__)
        
    *   [\_\_ror\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__ror__)
        
    *   [\_\_rpow\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__rpow__)
        
    *   [\_\_rsub\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__rsub__)
        
    *   [\_\_rtruediv\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__rtruediv__)
        
    *   [\_\_rxor\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__rxor__)
        
    *   [\_\_sub\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__sub__)
        
    *   [\_\_truediv\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__truediv__)
        
    *   [\_\_xor\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__xor__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.Variable Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#args_1)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#raises_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#attributes_1)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#child_classes_2)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#methods_2)
    *   [assign](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#assign)
        
    *   [assign\_add](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#assign_add)
        
    *   [assign\_sub](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#assign_sub)
        
    *   [batch\_scatter\_update](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#batch_scatter_update)
        
    *   [count\_up\_to](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#count_up_to)
        
    *   [eval](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#eval)
        
    *   [experimental\_ref](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#experimental_ref)
        
    *   [from\_proto](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#from_proto)
        
    *   [gather\_nd](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#gather_nd)
        
    *   [get\_shape](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#get_shape)
        
    *   [initialized\_value](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#initialized_value)
        
    *   [load](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#load)
        
    *   [read\_value](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#read_value)
        
    *   [ref](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#ref)
        
    *   [scatter\_add](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#scatter_add)
        
    *   [scatter\_div](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#scatter_div)
        
    *   [scatter\_max](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#scatter_max)
        
    *   [scatter\_min](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#scatter_min)
        
    *   [scatter\_mul](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#scatter_mul)
        
    *   [scatter\_nd\_add](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#scatter_nd_add)
        
    *   [scatter\_nd\_sub](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#scatter_nd_sub)
        
    *   [scatter\_nd\_update](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#scatter_nd_update)
        
    *   [scatter\_sub](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#scatter_sub)
        
    *   [scatter\_update](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#scatter_update)
        
    *   [set\_shape](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#set_shape)
        
    *   [sparse\_read](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#sparse_read)
        
    *   [to\_proto](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#to_proto)
        
    *   [value](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#value)
        
    *   [\_\_abs\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__abs__)
        
    *   [\_\_add\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__add__)
        
    *   [\_\_and\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__and__)
        
    *   [\_\_div\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__div__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__eq__)
        
    *   [\_\_floordiv\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__floordiv__)
        
    *   [\_\_ge\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__ge__)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__getitem__)
        
    *   [\_\_gt\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__gt__)
        
    *   [\_\_invert\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__invert__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__iter__)
        
    *   [\_\_le\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__le__)
        
    *   [\_\_lt\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__lt__)
        
    *   [\_\_matmul\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__matmul__)
        
    *   [\_\_mod\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__mod__)
        
    *   [\_\_mul\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__mul__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__ne__)
        
    *   [\_\_neg\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__neg__)
        
    *   [\_\_or\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__or__)
        
    *   [\_\_pow\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__pow__)
        
    *   [\_\_radd\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__radd__)
        
    *   [\_\_rand\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__rand__)
        
    *   [\_\_rdiv\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__rdiv__)
        
    *   [\_\_rfloordiv\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__rfloordiv__)
        
    *   [\_\_rmatmul\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__rmatmul__)
        
    *   [\_\_rmod\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__rmod__)
        
    *   [\_\_rmul\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__rmul__)
        
    *   [\_\_ror\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__ror__)
        
    *   [\_\_rpow\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__rpow__)
        
    *   [\_\_rsub\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__rsub__)
        
    *   [\_\_rtruediv\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__rtruediv__)
        
    *   [\_\_rxor\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__rxor__)
        
    *   [\_\_sub\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__sub__)
        
    *   [\_\_truediv\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__truediv__)
        
    *   [\_\_xor\_\_](https://www.tensorflow.org/api_docs/python/tf/Variable?version=stable#__xor__)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L206-L1396)

See the [variable guide](https://tensorflow.org/guide/variable)
.

tf.Variable(
        initial_value=None,
        trainable=None,
        validate_shape=True,
        caching_device=None,
        name=None,
        variable_def=None,
        dtype=None,
        import_scope=None,
        constraint=None,
        synchronization=tf.VariableSynchronization.AUTO,
        aggregation=tf.compat.v1.VariableAggregation.NONE,
        shape=None,
        experimental_enable_variable_lifting=True
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrating model checkpoints](https://www.tensorflow.org/guide/migrate/migrating_checkpoints)<br>    <br>*   [Introduction to gradients and automatic differentiation](https://www.tensorflow.org/guide/autodiff)<br>    <br>*   [Introduction to Variables](https://www.tensorflow.org/guide/variable)<br>    <br>*   [Advanced automatic differentiation](https://www.tensorflow.org/guide/advanced_autodiff)<br>    <br>*   [Better performance with tf.function](https://www.tensorflow.org/guide/function) | *   [Scalable model compression](https://www.tensorflow.org/tutorials/optimization/compression)<br>    <br>*   [Custom training loop with Keras and MultiWorkerMirroredStrategy](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_ctl)<br>    <br>*   [Neural style transfer](https://www.tensorflow.org/tutorials/generative/style_transfer)<br>    <br>*   [Learned data compression](https://www.tensorflow.org/tutorials/generative/data_compression)<br>    <br>*   [Learnable Distributions Zoo](https://www.tensorflow.org/probability/examples/Learnable_Distributions_Zoo) |

A variable maintains shared, persistent state manipulated by a program.

The `Variable()` constructor requires an initial value for the variable, which can be a `Tensor` of any type and shape. This initial value defines the type and shape of the variable. After construction, the type and shape of the variable are fixed. The value can be changed using one of the assign methods.

    v = tf.Variable(1.)

The `shape` argument to `Variable`'s constructor allows you to construct a variable with a less defined shape than its `initial_value`:

    v = tf.Variable(1., shape=tf.TensorShape(None))

Just like any `Tensor`, variables created with `Variable()` can be used as inputs to operations. Additionally, all the operators overloaded for the `Tensor` class are carried over to variables.

    w = tf.Variable([[1.], [2.]])

When building a machine learning model it is often convenient to distinguish between variables holding trainable model parameters and other variables such as a `step` variable used to count training steps. To make this easier, the variable constructor supports a `trainable=<bool>` parameter. [`tf.GradientTape`](https://www.tensorflow.org/api_docs/python/tf/GradientTape)
 watches trainable variables by default:

    with tf.GradientTape(persistent=True) as tape:

Variables are automatically tracked when assigned to attributes of types inheriting from [`tf.Module`](https://www.tensorflow.org/api_docs/python/tf/Module)
.

    m = tf.Module()

This tracking then allows saving variable values to [training checkpoints](https://www.tensorflow.org/guide/checkpoint)
, or to [SavedModels](https://www.tensorflow.org/guide/saved_model)
 which include serialized TensorFlow graphs.

Variables are often captured and manipulated by [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
s. This works the same way the un-decorated function would have:

    v = tf.Variable(0.)

Variables created inside a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 must be owned outside the function and be created only once:

    class M(tf.Module):

See the [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 documentation for details.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `initial_value` | A `Tensor`, or Python object convertible to a `Tensor`, which is the initial value for the Variable. The initial value must have a shape specified unless `validate_shape` is set to False. Can also be a callable with no argument that returns the initial value when called. In that case, `dtype` must be specified. (Note that initializer functions from init\_ops.py must first be bound to a shape before being used here.) |
| `trainable` | If `True`, GradientTapes automatically watch uses of this variable. Defaults to `True`, unless `synchronization` is set to `ON_READ`, in which case it defaults to `False`. |
| `validate_shape` | If `False`, allows the variable to be initialized with a value of unknown shape. If `True`, the default, the shape of `initial_value` must be known. |
| `caching_device` | Note: This argument is only valid when using a v1-style `Session`. Optional device string describing where the Variable should be cached for reading. Defaults to the Variable's device. If not `None`, caches on another device. Typical use is to cache on the device where the Ops using the Variable reside, to deduplicate copying through `Switch` and other conditional statements. |
| `name` | Optional name for the variable. Defaults to `'Variable'` and gets uniquified automatically. |
| `variable_def` | `VariableDef` protocol buffer. If not `None`, recreates the Variable object with its contents, referencing the variable's nodes in the graph, which must already exist. The graph is not changed. `variable_def` and the other arguments are mutually exclusive. |
| `dtype` | If set, initial\_value will be converted to the given type. If `None`, either the datatype will be kept (if `initial_value` is a Tensor), or `convert_to_tensor` will decide. |
| `import_scope` | Optional `string`. Name scope to add to the `Variable.` Only used when initializing from protocol buffer. |
| `constraint` | An optional projection function to be applied to the variable after being updated by an `Optimizer` (e.g. used to implement norm constraints or value constraints for layer weights). The function must take as input the unprojected Tensor representing the value of the variable and return the Tensor for the projected value (which must have the same shape). Constraints are not safe to use when doing asynchronous distributed training. |
| `synchronization` | Indicates when a distributed variable will be aggregated. Accepted values are constants defined in the class [`tf.VariableSynchronization`](https://www.tensorflow.org/api_docs/python/tf/VariableSynchronization)<br>. By default the synchronization is set to `AUTO` and the current `DistributionStrategy` chooses when to synchronize. |
| `aggregation` | Indicates how a distributed variable will be aggregated. Accepted values are constants defined in the class [`tf.VariableAggregation`](https://www.tensorflow.org/api_docs/python/tf/VariableAggregation)<br>. |
| `shape` | (optional) The shape of this variable. If None, the shape of `initial_value` will be used. When setting this argument to [`tf.TensorShape(None)`](https://www.tensorflow.org/api_docs/python/tf/TensorShape)<br> (representing an unspecified shape), the variable can be assigned with values of different shapes. |
| `experimental_enable_variable_lifting` | Whether to lift the variable out if it's in a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br>. Default is `True`. When this argument is `True`, variable creation will follow the behavior and restrictions described [here](https://www.tensorflow.org/guide/function#creating_tfvariables)<br>. If this argument is `False`, that description doesn't apply, and you can freely create and use the variable in the [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br>, as if it's a "mutable [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>". You can't return the variable though. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If both `variable_def` and initial\_value are specified. |
| `ValueError` | If the initial value is not specified, or does not have a shape and `validate_shape` is `True`. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `aggregation` |     |
| `constraint` | Returns the constraint function associated with this variable. |
| `device` | The device of this variable. |
| `dtype` | The `DType` of this variable. |
| `graph` | The `Graph` of this variable. |
| `initial_value` | Returns the Tensor used as the initial value for the variable.<br><br>Note that this is different from `initialized_value()` which runs the op that initializes the variable before returning its value. This method returns the tensor that is used by the op that initializes the variable. |
| `initializer` | The initializer operation for this variable. |
| `name` | The name of this variable. |
| `op` | The `Operation` of this variable. |
| `shape` | The `TensorShape` of this variable. |
| `synchronization` |     |
| `trainable` |     |

Child Classes
-------------

[`class SaveSliceInfo`](https://www.tensorflow.org/api_docs/python/tf/Variable/SaveSliceInfo)

Methods
-------

### `assign`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L522-L538)

assign(
        value, use_locking=False, name=None, read_value=True
    )

Assigns a new value to the variable.

This is essentially a shortcut for `assign(self, value)`.

|     |     |
| --- | --- |
| Args |     |
| `value` | A `Tensor`. The new value for this variable. |
| `use_locking` | If `True`, use locking during the assignment. |
| `name` | The name of the operation to be created |
| `read_value` | if True, will return something which evaluates to the new value of the variable; if False will return the assign op. |

|     |
| --- |
| Returns |     |
| The updated variable. If `read_value` is false, instead returns None in Eager mode and the assign op in graph mode. |     |

### `assign_add`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L540-L556)

assign_add(
        delta, use_locking=False, name=None, read_value=True
    )

Adds a value to this variable.

This is essentially a shortcut for `assign_add(self, delta)`.

|     |     |
| --- | --- |
| Args |     |
| `delta` | A `Tensor`. The value to add to this variable. |
| `use_locking` | If `True`, use locking during the operation. |
| `name` | The name of the operation to be created |
| `read_value` | if True, will return something which evaluates to the new value of the variable; if False will return the assign op. |

|     |
| --- |
| Returns |     |
| The updated variable. If `read_value` is false, instead returns None in Eager mode and the assign op in graph mode. |     |

### `assign_sub`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L558-L574)

assign_sub(
        delta, use_locking=False, name=None, read_value=True
    )

Subtracts a value from this variable.

This is essentially a shortcut for `assign_sub(self, delta)`.

|     |     |
| --- | --- |
| Args |     |
| `delta` | A `Tensor`. The value to subtract from this variable. |
| `use_locking` | If `True`, use locking during the operation. |
| `name` | The name of the operation to be created |
| `read_value` | if True, will return something which evaluates to the new value of the variable; if False will return the assign op. |

|     |
| --- |
| Returns |     |
| The updated variable. If `read_value` is false, instead returns None in Eager mode and the assign op in graph mode. |     |

### `batch_scatter_update`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L690-L734)

batch_scatter_update(
        sparse_delta, use_locking=False, name=None
    )

Assigns [`tf.IndexedSlices`](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices)
 to this variable batch-wise.

Analogous to `batch_gather`. This assumes that this variable and the sparse\_delta IndexedSlices have a series of leading dimensions that are the same for all of them, and the updates are performed on the last dimension of indices. In other words, the dimensions should be the following:

`num_prefix_dims = sparse_delta.indices.ndims - 1` `batch_dim = num_prefix_dims + 1` `sparse_delta.updates.shape = sparse_delta.indices.shape + var.shape[ batch_dim:]`

where

`sparse_delta.updates.shape[:num_prefix_dims]` `== sparse_delta.indices.shape[:num_prefix_dims]` `== var.shape[:num_prefix_dims]`

And the operation performed can be expressed as:

`var[i_1, ..., i_n, sparse_delta.indices[i_1, ..., i_n, j]] = sparse_delta.updates[ i_1, ..., i_n, j]`

When sparse\_delta.indices is a 1D tensor, this operation is equivalent to `scatter_update`.

To avoid this operation one can looping over the first `ndims` of the variable and using `scatter_update` on the subtensors that result of slicing the first dimension. This is a valid option for `ndims = 1`, but less efficient than this implementation.

|     |     |
| --- | --- |
| Args |     |
| `sparse_delta` | [`tf.IndexedSlices`](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices)<br> to be assigned to this variable. |
| `use_locking` | If `True`, use locking during the operation. |
| `name` | the name of the operation. |

|     |
| --- |
| Returns |     |
| The updated variable. |     |

|     |     |
| --- | --- |
| Raises |     |
| `TypeError` | if `sparse_delta` is not an `IndexedSlices`. |

### `count_up_to`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L905-L926)

count_up_to(
        limit
    )

Increments this variable until it reaches `limit`. (deprecated)

When that Op is run it tries to increment the variable by `1`. If incrementing the variable would bring it above `limit` then the Op raises the exception `OutOfRangeError`.

If no error is raised, the Op outputs the value of the variable before the increment.

This is essentially a shortcut for `count_up_to(self, limit)`.

|     |     |
| --- | --- |
| Args |     |
| `limit` | value at which incrementing the variable raises an error. |

|     |
| --- |
| Returns |     |
| A `Tensor` that will hold the variable value before the increment. If no other Op modifies this variable, the values produced will all be distinct. |     |

### `eval`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L442-L472)

eval(
        session=None
    )

In a session, computes and returns the value of this variable.

This is not a graph construction method, it does not add ops to the graph.

This convenience method requires a session where the graph containing this variable has been launched. If no session is passed, the default session is used. See [`tf.compat.v1.Session`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Session)
 for more information on launching a graph and on sessions.

v = tf.Variable([1, 2])
    init = tf.compat.v1.global_variables_initializer()
    
    with tf.compat.v1.Session() as sess:
        sess.run(init)
        # Usage passing the session explicitly.
        print(v.eval(sess))
        # Usage with the default session.  The 'with' block
        # above makes 'sess' the default session.
        print(v.eval())

|     |     |
| --- | --- |
| Args |     |
| `session` | The session to use to evaluate this variable. If none, the default session is used. |

|     |
| --- |
| Returns |     |
| A numpy `ndarray` with a copy of the value of this variable. |     |

### `experimental_ref`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L1159-L1161)

experimental_ref()

DEPRECATED FUNCTION

### `from_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L1143-L1146)

@staticmethod

Returns a `Variable` object created from `variable_def`.

### `gather_nd`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L890-L903)

gather_nd(
        indices, name=None
    )

Gather slices from `params` into a Tensor with shape specified by `indices`.

See tf.gather\_nd for details.

|     |     |
| --- | --- |
| Args |     |
| `indices` | A `Tensor`. Must be one of the following types: `int32`, `int64`. Index tensor. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns |     |
| A `Tensor`. Has the same type as `params`. |     |

### `get_shape`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L1123-L1125)

get_shape() -> tf.TensorShape

Alias of [`Variable.shape`](https://www.tensorflow.org/api_docs/python/tf/Variable#shape)
.

### `initialized_value`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L474-L496)

initialized_value()

Returns the value of the initialized variable. (deprecated)

You should use this instead of the variable itself to initialize another variable with a value that depends on the value of this variable.

# Initialize 'v' with a random tensor.
    v = tf.Variable(tf.random.truncated_normal([10, 40]))
    # Use `initialized_value` to guarantee that `v` has been
    # initialized before its value is used to initialize `w`.
    # The random values are picked only once.
    w = tf.Variable(v.initialized_value() * 2.0)

|     |
| --- |
| Returns |     |
| A `Tensor` holding the value of this variable after its initializer has run. |     |

### `load`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L928-L971)

load(
        value, session=None
    )

Load new value into this variable. (deprecated)

Writes new value to variable's memory. Doesn't add ops to the graph.

This convenience method requires a session where the graph containing this variable has been launched. If no session is passed, the default session is used. See [`tf.compat.v1.Session`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Session)
 for more information on launching a graph and on sessions.

v = tf.Variable([1, 2])
    init = tf.compat.v1.global_variables_initializer()
    
    with tf.compat.v1.Session() as sess:
        sess.run(init)
        # Usage passing the session explicitly.
        v.load([2, 3], sess)
        print(v.eval(sess)) # prints [2 3]
        # Usage with the default session.  The 'with' block
        # above makes 'sess' the default session.
        v.load([3, 4], sess)
        print(v.eval()) # prints [3 4]

|     |     |
| --- | --- |
| Args |     |
| `value` | New variable value |
| `session` | The session to use to evaluate this variable. If none, the default session is used. |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | Session is not passed and no default session |

### `read_value`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L411-L420)

read_value()

Returns the value of this variable, read in the current context.

Can be different from value() if it's on another device, with control dependencies, etc.

|     |
| --- |
| Returns |     |
| A `Tensor` containing the value of the variable. |     |

### `ref`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L1163-L1202)

ref()

Returns a hashable reference object to this Variable.

The primary use case for this API is to put variables in a set/dictionary. We can't put variables in a set/dictionary as `variable.__hash__()` is no longer available starting Tensorflow 2.0.

The following will raise an exception starting 2.0

    x = tf.Variable(5)

Instead, we can use `variable.ref()`.

    variable_set = {x.ref(), y.ref(), z.ref()}

Also, the reference object provides `.deref()` function that returns the original Variable.

    x = tf.Variable(5)

### `scatter_add`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L592-L606)

scatter_add(
        sparse_delta, use_locking=False, name=None
    )

Adds [`tf.IndexedSlices`](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices)
 to this variable.

|     |     |
| --- | --- |
| Args |     |
| `sparse_delta` | [`tf.IndexedSlices`](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices)<br> to be added to this variable. |
| `use_locking` | If `True`, use locking during the operation. |
| `name` | the name of the operation. |

|     |
| --- |
| Returns |     |
| The updated variable. |     |

|     |     |
| --- | --- |
| Raises |     |
| `TypeError` | if `sparse_delta` is not an `IndexedSlices`. |

### `scatter_div`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L658-L672)

scatter_div(
        sparse_delta, use_locking=False, name=None
    )

Divide this variable by [`tf.IndexedSlices`](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices)
.

|     |     |
| --- | --- |
| Args |     |
| `sparse_delta` | [`tf.IndexedSlices`](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices)<br> to divide this variable by. |
| `use_locking` | If `True`, use locking during the operation. |
| `name` | the name of the operation. |

|     |
| --- |
| Returns |     |
| The updated variable. |     |

|     |     |
| --- | --- |
| Raises |     |
| `TypeError` | if `sparse_delta` is not an `IndexedSlices`. |

### `scatter_max`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L608-L623)

scatter_max(
        sparse_delta, use_locking=False, name=None
    )

Updates this variable with the max of [`tf.IndexedSlices`](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices)
 and itself.

|     |     |
| --- | --- |
| Args |     |
| `sparse_delta` | [`tf.IndexedSlices`](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices)<br> to use as an argument of max with this variable. |
| `use_locking` | If `True`, use locking during the operation. |
| `name` | the name of the operation. |

|     |
| --- |
| Returns |     |
| The updated variable. |     |

|     |     |
| --- | --- |
| Raises |     |
| `TypeError` | if `sparse_delta` is not an `IndexedSlices`. |

### `scatter_min`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L625-L640)

scatter_min(
        sparse_delta, use_locking=False, name=None
    )

Updates this variable with the min of [`tf.IndexedSlices`](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices)
 and itself.

|     |     |
| --- | --- |
| Args |     |
| `sparse_delta` | [`tf.IndexedSlices`](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices)<br> to use as an argument of min with this variable. |
| `use_locking` | If `True`, use locking during the operation. |
| `name` | the name of the operation. |

|     |
| --- |
| Returns |     |
| The updated variable. |     |

|     |     |
| --- | --- |
| Raises |     |
| `TypeError` | if `sparse_delta` is not an `IndexedSlices`. |

### `scatter_mul`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L642-L656)

scatter_mul(
        sparse_delta, use_locking=False, name=None
    )

Multiply this variable by [`tf.IndexedSlices`](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices)
.

|     |     |
| --- | --- |
| Args |     |
| `sparse_delta` | [`tf.IndexedSlices`](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices)<br> to multiply this variable by. |
| `use_locking` | If `True`, use locking during the operation. |
| `name` | the name of the operation. |

|     |
| --- |
| Returns |     |
| The updated variable. |     |

|     |     |
| --- | --- |
| Raises |     |
| `TypeError` | if `sparse_delta` is not an `IndexedSlices`. |

### `scatter_nd_add`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L782-L826)

scatter_nd_add(
        indices, updates, name=None
    )

Applies sparse addition to individual values or slices in a Variable.

The Variable has rank `P` and `indices` is a `Tensor` of rank `Q`.

`indices` must be integer tensor, containing indices into self. It must be shape `[d_0, ..., d_{Q-2}, K]` where `0 < K <= P`.

The innermost dimension of `indices` (with length `K`) corresponds to indices into elements (if `K = P`) or slices (if `K < P`) along the `K`th dimension of self.

`updates` is `Tensor` of rank `Q-1+P-K` with shape:

[d_0, ..., d_{Q-2}, self.shape[K], ..., self.shape[P-1]].

For example, say we want to add 4 scattered elements to a rank-1 tensor to 8 elements. In Python, that update would look like this:

    v = tf.Variable([1, 2, 3, 4, 5, 6, 7, 8])
        indices = tf.constant([[4], [3], [1] ,[7]])
        updates = tf.constant([9, 10, 11, 12])
        v.scatter_nd_add(indices, updates)
        print(v)

The resulting update to v would look like this:

[1, 13, 3, 14, 14, 6, 7, 20]

See [`tf.scatter_nd`](https://www.tensorflow.org/api_docs/python/tf/scatter_nd)
 for more details about how to make updates to slices.

|     |     |
| --- | --- |
| Args |     |
| `indices` | The indices to be used in the operation. |
| `updates` | The values to be used in the operation. |
| `name` | the name of the operation. |

|     |
| --- |
| Returns |     |
| The updated variable. |     |

### `scatter_nd_sub`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L736-L780)

scatter_nd_sub(
        indices, updates, name=None
    )

Applies sparse subtraction to individual values or slices in a Variable.

Assuming the variable has rank `P` and `indices` is a `Tensor` of rank `Q`.

`indices` must be integer tensor, containing indices into self. It must be shape `[d_0, ..., d_{Q-2}, K]` where `0 < K <= P`.

The innermost dimension of `indices` (with length `K`) corresponds to indices into elements (if `K = P`) or slices (if `K < P`) along the `K`th dimension of self.

`updates` is `Tensor` of rank `Q-1+P-K` with shape:

[d_0, ..., d_{Q-2}, self.shape[K], ..., self.shape[P-1]].

For example, say we want to add 4 scattered elements to a rank-1 tensor to 8 elements. In Python, that update would look like this:

    v = tf.Variable([1, 2, 3, 4, 5, 6, 7, 8])
        indices = tf.constant([[4], [3], [1] ,[7]])
        updates = tf.constant([9, 10, 11, 12])
        v.scatter_nd_sub(indices, updates)
        print(v)

After the update `v` would look like this:

[1, -9, 3, -6, -4, 6, 7, -4]

See [`tf.scatter_nd`](https://www.tensorflow.org/api_docs/python/tf/scatter_nd)
 for more details about how to make updates to slices.

|     |     |
| --- | --- |
| Args |     |
| `indices` | The indices to be used in the operation. |
| `updates` | The values to be used in the operation. |
| `name` | the name of the operation. |

|     |
| --- |
| Returns |     |
| The updated variable. |     |

### `scatter_nd_update`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L828-L872)

scatter_nd_update(
        indices, updates, name=None
    )

Applies sparse assignment to individual values or slices in a Variable.

The Variable has rank `P` and `indices` is a `Tensor` of rank `Q`.

`indices` must be integer tensor, containing indices into self. It must be shape `[d_0, ..., d_{Q-2}, K]` where `0 < K <= P`.

The innermost dimension of `indices` (with length `K`) corresponds to indices into elements (if `K = P`) or slices (if `K < P`) along the `K`th dimension of self.

`updates` is `Tensor` of rank `Q-1+P-K` with shape:

[d_0, ..., d_{Q-2}, self.shape[K], ..., self.shape[P-1]].

For example, say we want to add 4 scattered elements to a rank-1 tensor to 8 elements. In Python, that update would look like this:

    v = tf.Variable([1, 2, 3, 4, 5, 6, 7, 8])
        indices = tf.constant([[4], [3], [1] ,[7]])
        updates = tf.constant([9, 10, 11, 12])
        v.scatter_nd_update(indices, updates)
        print(v)

The resulting update to v would look like this:

[1, 11, 3, 10, 9, 6, 7, 12]

See [`tf.scatter_nd`](https://www.tensorflow.org/api_docs/python/tf/scatter_nd)
 for more details about how to make updates to slices.

|     |     |
| --- | --- |
| Args |     |
| `indices` | The indices to be used in the operation. |
| `updates` | The values to be used in the operation. |
| `name` | the name of the operation. |

|     |
| --- |
| Returns |     |
| The updated variable. |     |

### `scatter_sub`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L576-L590)

scatter_sub(
        sparse_delta, use_locking=False, name=None
    )

Subtracts [`tf.IndexedSlices`](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices)
 from this variable.

|     |     |
| --- | --- |
| Args |     |
| `sparse_delta` | [`tf.IndexedSlices`](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices)<br> to be subtracted from this variable. |
| `use_locking` | If `True`, use locking during the operation. |
| `name` | the name of the operation. |

|     |
| --- |
| Returns |     |
| The updated variable. |     |

|     |     |
| --- | --- |
| Raises |     |
| `TypeError` | if `sparse_delta` is not an `IndexedSlices`. |

### `scatter_update`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L674-L688)

scatter_update(
        sparse_delta, use_locking=False, name=None
    )

Assigns [`tf.IndexedSlices`](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices)
 to this variable.

|     |     |
| --- | --- |
| Args |     |
| `sparse_delta` | [`tf.IndexedSlices`](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices)<br> to be assigned to this variable. |
| `use_locking` | If `True`, use locking during the operation. |
| `name` | the name of the operation. |

|     |
| --- |
| Returns |     |
| The updated variable. |     |

|     |     |
| --- | --- |
| Raises |     |
| `TypeError` | if `sparse_delta` is not an `IndexedSlices`. |

### `set_shape`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L422-L428)

set_shape(
        shape
    )

Overrides the shape for this variable.

|     |     |
| --- | --- |
| Args |     |
| `shape` | the `TensorShape` representing the overridden shape. |

### `sparse_read`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L874-L888)

sparse_read(
        indices, name=None
    )

Gather slices from params axis axis according to indices.

This function supports a subset of tf.gather, see tf.gather for details on usage.

|     |     |
| --- | --- |
| Args |     |
| `indices` | The index `Tensor`. Must be one of the following types: `int32`, `int64`. Must be in range `[0, params.shape[axis])`. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A `Tensor`. Has the same type as `params`. |     |\
\
### `to_proto`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L1131-L1141)\
\
to_proto(\
        export_scope=None\
    )\
\
Converts a `Variable` to a `VariableDef` protocol buffer.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `export_scope` | Optional `string`. Name scope to remove. |\
\
|     |\
| --- |\
| Returns |     |\
| A `VariableDef` protocol buffer, or `None` if the `Variable` is not in the specified name scope. |     |\
\
### `value`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L392-L409)\
\
value()\
\
Returns the last snapshot of this variable.\
\
You usually do not need to call this method as all ops that need the value of the variable call it automatically through a `convert_to_tensor()` call.\
\
Returns a `Tensor` which holds the value of the variable. You can not assign a new value to this tensor as it is not a reference to the variable.\
\
To avoid copies, if the consumer of the returned value is on the same device as the variable, this actually returns the live value of the variable, not a copy. Updates to the variable are seen by the consumer. If the consumer is on a different device it will get a copy of the variable.\
\
|     |\
| --- |\
| Returns |     |\
| A `Tensor` containing the value of the variable. |     |\
\
### `__abs__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/tensor_math_operator_overrides.py#L141-L144)\
\
__abs__(\
        name=None\
    )\
\
### `__add__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L105-L131)\
\
__add__(\
        y\
    )\
\
### `__and__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L105-L131)\
\
__and__(\
        y\
    )\
\
### `__div__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L105-L131)\
\
__div__(\
        y\
    )\
\
### `__eq__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L1036-L1045)\
\
__eq__(\
        other\
    )\
\
Compares two variables element-wise for equality.\
\
### `__floordiv__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L105-L131)\
\
__floordiv__(\
        y\
    )\
\
### `__ge__`\
\
__ge__(\
        y: Annotated[Any, tf.raw_ops.Any],\
        name=None\
    ) -> Annotated[Any, tf.raw_ops.Any]\
\
Returns the truth value of (x >= y) element-wise.\
\
#### Example:\
\
x = tf.constant([5, 4, 6, 7])\
    y = tf.constant([5, 2, 5, 10])\
    tf.math.greater_equal(x, y) ==> [True, True, True, False]\
    \
    x = tf.constant([5, 4, 6, 7])\
    y = tf.constant([5])\
    tf.math.greater_equal(x, y) ==> [True, False, True, True]\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`. |\
| `y` | A `Tensor`. Must have the same type as `x`. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A `Tensor` of type `bool`. |     |\
\
### `__getitem__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/tensor_getitem_override.py#L270-L311)\
\
__getitem__(\
        slice_spec\
    )\
\
Creates a slice helper object given a variable.\
\
This allows creating a sub-tensor from part of the current contents of a variable. See [`tf.Tensor.**getitem**`](https://www.tensorflow.org/api_docs/python/tf/Tensor#__getitem__)\
 for detailed examples of slicing.\
\
This function in addition also allows assignment to a sliced range. This is similar to `__setitem__` functionality in Python. However, the syntax is different so that the user can capture the assignment operation for grouping or passing to `sess.run()` in TF1. For example,\
\
import tensorflow as tf\
    A = tf.Variable([[1,2,3], [4,5,6], [7,8,9]], dtype=tf.float32)\
    print(A[:2, :2])  # => [[1,2], [4,5]]\
    \
    A[:2,:2].assign(22. * tf.ones((2, 2))))\
    print(A) # => [[22, 22, 3], [22, 22, 6], [7,8,9]]\
\
Note that assignments currently do not support NumPy broadcasting semantics.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `var` | An `ops.Variable` object. |\
| `slice_spec` | The arguments to [`Tensor.**getitem**`](https://www.tensorflow.org/api_docs/python/tf/Tensor#__getitem__)<br>. |\
\
|     |\
| --- |\
| Returns |     |\
| The appropriate slice of "tensor", based on "slice\_spec". As an operator. The operator also has a `assign()` method that can be used to generate an assignment operator. |     |\
\
|     |     |\
| --- | --- |\
| Raises |     |\
| `ValueError` | If a slice range is negative size. |\
| `TypeError` | TypeError: If the slice indices aren't int, slice, ellipsis, tf.newaxis or int32/int64 tensors. |\
\
### `__gt__`\
\
__gt__(\
        y: Annotated[Any, tf.raw_ops.Any],\
        name=None\
    ) -> Annotated[Any, tf.raw_ops.Any]\
\
Returns the truth value of (x > y) element-wise.\
\
#### Example:\
\
x = tf.constant([5, 4, 6])\
    y = tf.constant([5, 2, 5])\
    tf.math.greater(x, y) ==> [False, True, True]\
    \
    x = tf.constant([5, 4, 6])\
    y = tf.constant([5])\
    tf.math.greater(x, y) ==> [False, False, True]\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`. |\
| `y` | A `Tensor`. Must have the same type as `x`. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A `Tensor` of type `bool`. |     |\
\
### `__invert__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/tensor_math_operator_overrides.py#L135-L138)\
\
__invert__(\
        name=None\
    )\
\
### `__iter__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L1059-L1061)\
\
__iter__()\
\
When executing eagerly, iterates over the value of the variable.\
\
### `__le__`\
\
__le__(\
        y: Annotated[Any, tf.raw_ops.Any],\
        name=None\
    ) -> Annotated[Any, tf.raw_ops.Any]\
\
Returns the truth value of (x <= y) element-wise.\
\
#### Example:\
\
x = tf.constant([5, 4, 6])\
    y = tf.constant([5])\
    tf.math.less_equal(x, y) ==> [True, True, False]\
    \
    x = tf.constant([5, 4, 6])\
    y = tf.constant([5, 6, 6])\
    tf.math.less_equal(x, y) ==> [True, True, True]\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`. |\
| `y` | A `Tensor`. Must have the same type as `x`. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A `Tensor` of type `bool`. |     |\
\
### `__lt__`\
\
__lt__(\
        y: Annotated[Any, tf.raw_ops.Any],\
        name=None\
    ) -> Annotated[Any, tf.raw_ops.Any]\
\
Returns the truth value of (x < y) element-wise.\
\
#### Example:\
\
x = tf.constant([5, 4, 6])\
    y = tf.constant([5])\
    tf.math.less(x, y) ==> [False, True, False]\
    \
    x = tf.constant([5, 4, 6])\
    y = tf.constant([5, 6, 7])\
    tf.math.less(x, y) ==> [False, True, True]\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`. |\
| `y` | A `Tensor`. Must have the same type as `x`. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A `Tensor` of type `bool`. |     |\
\
### `__matmul__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L105-L131)\
\
__matmul__(\
        y\
    )\
\
### `__mod__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L105-L131)\
\
__mod__(\
        y\
    )\
\
### `__mul__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L105-L131)\
\
__mul__(\
        y\
    )\
\
### `__ne__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L1048-L1057)\
\
__ne__(\
        other\
    )\
\
Compares two variables element-wise for equality.\
\
### `__neg__`\
\
__neg__(\
        name=None\
    ) -> Annotated[Any, tf.raw_ops.Any]\
\
Computes numerical negative value element-wise.\
\
I.e., y\=−x.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int8`, `int16`, `int32`, `int64`, `complex64`, `complex128`. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A `Tensor`. Has the same type as `x`. |     |\
\
### `__or__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L105-L131)\
\
__or__(\
        y\
    )\
\
### `__pow__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L105-L131)\
\
__pow__(\
        y\
    )\
\
### `__radd__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L144-L150)\
\
__radd__(\
        x\
    )\
\
### `__rand__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L144-L150)\
\
__rand__(\
        x\
    )\
\
### `__rdiv__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L144-L150)\
\
__rdiv__(\
        x\
    )\
\
### `__rfloordiv__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L144-L150)\
\
__rfloordiv__(\
        x\
    )\
\
### `__rmatmul__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L144-L150)\
\
__rmatmul__(\
        x\
    )\
\
### `__rmod__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L144-L150)\
\
__rmod__(\
        x\
    )\
\
### `__rmul__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L144-L150)\
\
__rmul__(\
        x\
    )\
\
### `__ror__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L144-L150)\
\
__ror__(\
        x\
    )\
\
### `__rpow__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L144-L150)\
\
__rpow__(\
        x\
    )\
\
### `__rsub__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L144-L150)\
\
__rsub__(\
        x\
    )\
\
### `__rtruediv__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L144-L150)\
\
__rtruediv__(\
        x\
    )\
\
### `__rxor__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L144-L150)\
\
__rxor__(\
        x\
    )\
\
### `__sub__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L105-L131)\
\
__sub__(\
        y\
    )\
\
### `__truediv__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L105-L131)\
\
__truediv__(\
        y\
    )\
\
### `__xor__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L105-L131)\
\
__xor__(\
        y\
    )\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.