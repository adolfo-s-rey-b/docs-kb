[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fexperimental%2Fdtensor%2FDVariable%3Fversion%3Dstable&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#used-in-the-notebooks_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#attributes_1)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#child_classes_2)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#methods_2)
    *   [assign](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#assign)
        
    *   [assign\_add](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#assign_add)
        
    *   [assign\_sub](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#assign_sub)
        
    *   [batch\_scatter\_update](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#batch_scatter_update)
        
    *   [count\_up\_to](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#count_up_to)
        
    *   [eval](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#eval)
        
    *   [experimental\_ref](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#experimental_ref)
        
    *   [from\_proto](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#from_proto)
        
    *   [gather\_nd](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#gather_nd)
        
    *   [get\_shape](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#get_shape)
        
    *   [initialized\_value](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#initialized_value)
        
    *   [is\_initialized](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#is_initialized)
        
    *   [load](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#load)
        
    *   [numpy](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#numpy)
        
    *   [read\_value](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#read_value)
        
    *   [read\_value\_no\_copy](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#read_value_no_copy)
        
    *   [ref](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#ref)
        
    *   [scatter\_add](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#scatter_add)
        
    *   [scatter\_div](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#scatter_div)
        
    *   [scatter\_max](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#scatter_max)
        
    *   [scatter\_min](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#scatter_min)
        
    *   [scatter\_mul](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#scatter_mul)
        
    *   [scatter\_nd\_add](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#scatter_nd_add)
        
    *   [scatter\_nd\_max](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#scatter_nd_max)
        
    *   [scatter\_nd\_min](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#scatter_nd_min)
        
    *   [scatter\_nd\_sub](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#scatter_nd_sub)
        
    *   [scatter\_nd\_update](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#scatter_nd_update)
        
    *   [scatter\_sub](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#scatter_sub)
        
    *   [scatter\_update](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#scatter_update)
        
    *   [set\_shape](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#set_shape)
        
    *   [sparse\_read](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#sparse_read)
        
    *   [to\_proto](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#to_proto)
        
    *   [value](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#value)
        
    *   [\_\_abs\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__abs__)
        
    *   [\_\_add\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__add__)
        
    *   [\_\_and\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__and__)
        
    *   [\_\_array\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__array__)
        
    *   [\_\_bool\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__bool__)
        
    *   [\_\_div\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__div__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__eq__)
        
    *   [\_\_floordiv\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__floordiv__)
        
    *   [\_\_ge\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__ge__)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__getitem__)
        
    *   [\_\_gt\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__gt__)
        
    *   [\_\_invert\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__invert__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__iter__)
        
    *   [\_\_le\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__le__)
        
    *   [\_\_lt\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__lt__)
        
    *   [\_\_matmul\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__matmul__)
        
    *   [\_\_mod\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__mod__)
        
    *   [\_\_mul\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__mul__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__ne__)
        
    *   [\_\_neg\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__neg__)
        
    *   [\_\_nonzero\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__nonzero__)
        
    *   [\_\_or\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__or__)
        
    *   [\_\_pow\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__pow__)
        
    *   [\_\_radd\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__radd__)
        
    *   [\_\_rand\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__rand__)
        
    *   [\_\_rdiv\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__rdiv__)
        
    *   [\_\_rfloordiv\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__rfloordiv__)
        
    *   [\_\_rmatmul\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__rmatmul__)
        
    *   [\_\_rmod\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__rmod__)
        
    *   [\_\_rmul\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__rmul__)
        
    *   [\_\_ror\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__ror__)
        
    *   [\_\_rpow\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__rpow__)
        
    *   [\_\_rsub\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__rsub__)
        
    *   [\_\_rtruediv\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__rtruediv__)
        
    *   [\_\_rxor\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__rxor__)
        
    *   [\_\_sub\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__sub__)
        
    *   [\_\_truediv\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__truediv__)
        
    *   [\_\_xor\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__xor__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.dtensor.DVariable Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#used-in-the-notebooks_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#attributes_1)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#child_classes_2)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#methods_2)
    *   [assign](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#assign)
        
    *   [assign\_add](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#assign_add)
        
    *   [assign\_sub](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#assign_sub)
        
    *   [batch\_scatter\_update](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#batch_scatter_update)
        
    *   [count\_up\_to](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#count_up_to)
        
    *   [eval](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#eval)
        
    *   [experimental\_ref](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#experimental_ref)
        
    *   [from\_proto](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#from_proto)
        
    *   [gather\_nd](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#gather_nd)
        
    *   [get\_shape](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#get_shape)
        
    *   [initialized\_value](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#initialized_value)
        
    *   [is\_initialized](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#is_initialized)
        
    *   [load](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#load)
        
    *   [numpy](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#numpy)
        
    *   [read\_value](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#read_value)
        
    *   [read\_value\_no\_copy](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#read_value_no_copy)
        
    *   [ref](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#ref)
        
    *   [scatter\_add](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#scatter_add)
        
    *   [scatter\_div](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#scatter_div)
        
    *   [scatter\_max](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#scatter_max)
        
    *   [scatter\_min](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#scatter_min)
        
    *   [scatter\_mul](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#scatter_mul)
        
    *   [scatter\_nd\_add](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#scatter_nd_add)
        
    *   [scatter\_nd\_max](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#scatter_nd_max)
        
    *   [scatter\_nd\_min](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#scatter_nd_min)
        
    *   [scatter\_nd\_sub](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#scatter_nd_sub)
        
    *   [scatter\_nd\_update](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#scatter_nd_update)
        
    *   [scatter\_sub](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#scatter_sub)
        
    *   [scatter\_update](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#scatter_update)
        
    *   [set\_shape](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#set_shape)
        
    *   [sparse\_read](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#sparse_read)
        
    *   [to\_proto](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#to_proto)
        
    *   [value](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#value)
        
    *   [\_\_abs\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__abs__)
        
    *   [\_\_add\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__add__)
        
    *   [\_\_and\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__and__)
        
    *   [\_\_array\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__array__)
        
    *   [\_\_bool\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__bool__)
        
    *   [\_\_div\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__div__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__eq__)
        
    *   [\_\_floordiv\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__floordiv__)
        
    *   [\_\_ge\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__ge__)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__getitem__)
        
    *   [\_\_gt\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__gt__)
        
    *   [\_\_invert\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__invert__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__iter__)
        
    *   [\_\_le\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__le__)
        
    *   [\_\_lt\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__lt__)
        
    *   [\_\_matmul\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__matmul__)
        
    *   [\_\_mod\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__mod__)
        
    *   [\_\_mul\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__mul__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__ne__)
        
    *   [\_\_neg\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__neg__)
        
    *   [\_\_nonzero\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__nonzero__)
        
    *   [\_\_or\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__or__)
        
    *   [\_\_pow\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__pow__)
        
    *   [\_\_radd\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__radd__)
        
    *   [\_\_rand\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__rand__)
        
    *   [\_\_rdiv\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__rdiv__)
        
    *   [\_\_rfloordiv\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__rfloordiv__)
        
    *   [\_\_rmatmul\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__rmatmul__)
        
    *   [\_\_rmod\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__rmod__)
        
    *   [\_\_rmul\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__rmul__)
        
    *   [\_\_ror\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__ror__)
        
    *   [\_\_rpow\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__rpow__)
        
    *   [\_\_rsub\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__rsub__)
        
    *   [\_\_rtruediv\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__rtruediv__)
        
    *   [\_\_rxor\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__rxor__)
        
    *   [\_\_sub\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__sub__)
        
    *   [\_\_truediv\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__truediv__)
        
    *   [\_\_xor\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable?version=stable#__xor__)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/d_variable.py#L143-L260)

A replacement for tf.Variable which follows initial value placement.

Inherits From: [`Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)

tf.experimental.dtensor.DVariable(
        initial_value, *args, dtype=None, **kwargs
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Distributed training with Core APIs and DTensor](https://www.tensorflow.org/guide/core/distribution)<br>    <br>*   [DTensor concepts](https://www.tensorflow.org/guide/dtensor_overview) | *   [Distributed training with DTensors](https://www.tensorflow.org/tutorials/distribute/dtensor_ml_tutorial) |

The class also handles restore/save operations in DTensor. Note that, DVariable may fall back to normal tf.Variable at this moment if `initial_value` is not a DTensor.

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `aggregation` |     |
| `constraint` | Returns the constraint function associated with this variable. |
| `create` | The op responsible for initializing this variable. |
| `device` | The device this variable is on. |
| `dtype` | The dtype of this variable. |
| `graph` | The `Graph` of this variable. |
| `handle` | The handle by which this variable can be accessed. |
| `initial_value` | Returns the Tensor used as the initial value for the variable. |
| `initializer` | The op responsible for initializing this variable. |
| `name` | The name of the handle for this variable. |
| `op` | The op for this variable. |
| `save_as_bf16` |     |
| `shape` | The shape of this variable. |
| `synchronization` |     |
| `trainable` |     |

Child Classes
-------------

[`class SaveSliceInfo`](https://www.tensorflow.org/api_docs/python/tf/Variable/SaveSliceInfo)

Methods
-------

### `assign`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/resource_variable_ops.py#L1063-L1102)

assign(
        value, use_locking=None, name=None, read_value=True
    )

Assigns a new value to this variable.

|     |     |
| --- | --- |
| Args |     |
| `value` | A `Tensor`. The new value for this variable. |
| `use_locking` | If `True`, use locking during the assignment. |
| `name` | The name to use for the assignment. |
| `read_value` | A `bool`. Whether to read and return the new value of the variable or not. |

|     |
| --- |
| Returns |     |
| If `read_value` is `True`, this method will return the new value of the variable after the assignment has completed. Otherwise, when in graph mode it will return the `Operation` that does the assignment, and when in eager mode it will return `None`. |     |

### `assign_add`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/resource_variable_ops.py#L1028-L1051)

assign_add(
        delta, use_locking=None, name=None, read_value=True
    )

Adds a value to this variable.

|     |     |
| --- | --- |
| Args |     |
| `delta` | A `Tensor`. The value to add to this variable. |
| `use_locking` | If `True`, use locking during the operation. |
| `name` | The name to use for the operation. |
| `read_value` | A `bool`. Whether to read and return the new value of the variable or not. |

|     |
| --- |
| Returns |     |
| If `read_value` is `True`, this method will return the new value of the variable after the assignment has completed. Otherwise, when in graph mode it will return the `Operation` that does the assignment, and when in eager mode it will return `None`. |     |

### `assign_sub`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/resource_variable_ops.py#L1000-L1026)

assign_sub(
        delta, use_locking=None, name=None, read_value=True
    )

Subtracts a value from this variable.

|     |     |
| --- | --- |
| Args |     |
| `delta` | A `Tensor`. The value to subtract from this variable. |
| `use_locking` | If `True`, use locking during the operation. |
| `name` | The name to use for the operation. |
| `read_value` | A `bool`. Whether to read and return the new value of the variable or not. |

|     |
| --- |
| Returns |     |
| If `read_value` is `True`, this method will return the new value of the variable after the assignment has completed. Otherwise, when in graph mode it will return the `Operation` that does the assignment, and when in eager mode it will return `None`. |     |

### `batch_scatter_update`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/resource_variable_ops.py#L1285-L1338)

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/resource_variable_ops.py#L717-L739)

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/resource_variable_ops.py#L704-L709)

eval(
        session=None
    )

Evaluates and returns the value of this variable.

### `experimental_ref`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L1159-L1161)

experimental_ref()

DEPRECATED FUNCTION

### `from_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/resource_variable_ops.py#L977-L983)

@staticmethod

Returns a `Variable` object created from `variable_def`.

### `gather_nd`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/resource_variable_ops.py#L921-L929)

gather_nd(
        indices, name=None
    )

Reads the value of this variable sparsely, using `gather_nd`.

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

### `is_initialized`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/resource_variable_ops.py#L987-L998)

is_initialized(
        name=None
    )

Checks whether a resource variable has been initialized.

Outputs boolean scalar indicating whether the tensor has been initialized.

|     |     |
| --- | --- |
| Args |     |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns |     |
| A `Tensor` of type `bool`. |     |

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

### `numpy`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/resource_variable_ops.py#L711-L715)

numpy()

### `read_value`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/resource_variable_ops.py#L871-L884)

read_value()

Constructs an op which reads the value of this variable.

Should be used when there are multiple reads, or when it is desirable to read the value only after some condition is true.

|     |
| --- |
| Returns |     |
| The value of the variable. |     |

### `read_value_no_copy`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/resource_variable_ops.py#L886-L900)

read_value_no_copy()

Constructs an op which reads the value of this variable without copy.

The variable is read without making a copy even when it has been sparsely accessed. Variables in copy-on-read mode will be converted to copy-on-write mode.

|     |
| --- |
| Returns |     |
| The value of the variable. |     |

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/resource_variable_ops.py#L1139-L1161)

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/resource_variable_ops.py#L1237-L1259)

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/resource_variable_ops.py#L1163-L1186)

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/resource_variable_ops.py#L1188-L1211)

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/resource_variable_ops.py#L1213-L1235)

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/resource_variable_ops.py#L1392-L1442)

scatter_nd_add(
        indices, updates, name=None
    )

Applies sparse addition to individual values or slices in a Variable.

`ref` is a `Tensor` with rank `P` and `indices` is a `Tensor` of rank `Q`.

`indices` must be integer tensor, containing indices into `ref`. It must be shape `[d_0, ..., d_{Q-2}, K]` where `0 < K <= P`.

The innermost dimension of `indices` (with length `K`) corresponds to indices into elements (if `K = P`) or slices (if `K < P`) along the `K`th dimension of `ref`.

`updates` is `Tensor` of rank `Q-1+P-K` with shape:

[d_0, ..., d_{Q-2}, ref.shape[K], ..., ref.shape[P-1]].

For example, say we want to add 4 scattered elements to a rank-1 tensor to 8 elements. In Python, that update would look like this:

    ref = tf.Variable([1, 2, 3, 4, 5, 6, 7, 8])
        indices = tf.constant([[4], [3], [1] ,[7]])
        updates = tf.constant([9, 10, 11, 12])
        add = ref.scatter_nd_add(indices, updates)
        with tf.compat.v1.Session() as sess:
          print sess.run(add)

The resulting update to ref would look like this:

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

### `scatter_nd_max`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/resource_variable_ops.py#L1496-L1530)

scatter_nd_max(
        indices, updates, name=None
    )

Updates this variable with the max of [`tf.IndexedSlices`](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices)
 and itself.

`ref` is a `Tensor` with rank `P` and `indices` is a `Tensor` of rank `Q`.

`indices` must be integer tensor, containing indices into `ref`. It must be shape `[d_0, ..., d_{Q-2}, K]` where `0 < K <= P`.

The innermost dimension of `indices` (with length `K`) corresponds to indices into elements (if `K = P`) or slices (if `K < P`) along the `K`th dimension of `ref`.

`updates` is `Tensor` of rank `Q-1+P-K` with shape:

[d_0, ..., d_{Q-2}, ref.shape[K], ..., ref.shape[P-1]].

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

### `scatter_nd_min`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/resource_variable_ops.py#L1532-L1566)

scatter_nd_min(
        indices, updates, name=None
    )

Updates this variable with the min of [`tf.IndexedSlices`](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices)
 and itself.

`ref` is a `Tensor` with rank `P` and `indices` is a `Tensor` of rank `Q`.

`indices` must be integer tensor, containing indices into `ref`. It must be shape `[d_0, ..., d_{Q-2}, K]` where `0 < K <= P`.

The innermost dimension of `indices` (with length `K`) corresponds to indices into elements (if `K = P`) or slices (if `K < P`) along the `K`th dimension of `ref`.

`updates` is `Tensor` of rank `Q-1+P-K` with shape:

[d_0, ..., d_{Q-2}, ref.shape[K], ..., ref.shape[P-1]].

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/resource_variable_ops.py#L1340-L1390)

scatter_nd_sub(
        indices, updates, name=None
    )

Applies sparse subtraction to individual values or slices in a Variable.

`ref` is a `Tensor` with rank `P` and `indices` is a `Tensor` of rank `Q`.

`indices` must be integer tensor, containing indices into `ref`. It must be shape `[d_0, ..., d_{Q-2}, K]` where `0 < K <= P`.

The innermost dimension of `indices` (with length `K`) corresponds to indices into elements (if `K = P`) or slices (if `K < P`) along the `K`th dimension of `ref`.

`updates` is `Tensor` of rank `Q-1+P-K` with shape:

[d_0, ..., d_{Q-2}, ref.shape[K], ..., ref.shape[P-1]].

For example, say we want to add 4 scattered elements to a rank-1 tensor to 8 elements. In Python, that update would look like this:

    ref = tf.Variable([1, 2, 3, 4, 5, 6, 7, 8])
        indices = tf.constant([[4], [3], [1] ,[7]])
        updates = tf.constant([9, 10, 11, 12])
        op = ref.scatter_nd_sub(indices, updates)
        with tf.compat.v1.Session() as sess:
          print sess.run(op)

The resulting update to ref would look like this:

[1, -9, 3, -6, -6, 6, 7, -4]

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/resource_variable_ops.py#L1444-L1494)

scatter_nd_update(
        indices, updates, name=None
    )

Applies sparse assignment to individual values or slices in a Variable.

`ref` is a `Tensor` with rank `P` and `indices` is a `Tensor` of rank `Q`.

`indices` must be integer tensor, containing indices into `ref`. It must be shape `[d_0, ..., d_{Q-2}, K]` where `0 < K <= P`.

The innermost dimension of `indices` (with length `K`) corresponds to indices into elements (if `K = P`) or slices (if `K < P`) along the `K`th dimension of `ref`.

`updates` is `Tensor` of rank `Q-1+P-K` with shape:

[d_0, ..., d_{Q-2}, ref.shape[K], ..., ref.shape[P-1]].

For example, say we want to add 4 scattered elements to a rank-1 tensor to 8 elements. In Python, that update would look like this:

    ref = tf.Variable([1, 2, 3, 4, 5, 6, 7, 8])
        indices = tf.constant([[4], [3], [1] ,[7]])
        updates = tf.constant([9, 10, 11, 12])
        op = ref.scatter_nd_update(indices, updates)
        with tf.compat.v1.Session() as sess:
          print sess.run(op)

The resulting update to ref would look like this:

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/resource_variable_ops.py#L1115-L1137)

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/resource_variable_ops.py#L1261-L1283)

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/resource_variable_ops.py#L626-L627)

set_shape(
        shape
    )

Overrides the shape for this variable.

|     |     |
| --- | --- |
| Args |     |
| `shape` | the `TensorShape` representing the overridden shape. |

### `sparse_read`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/resource_variable_ops.py#L902-L919)

sparse_read(
        indices, name=None
    )

Reads the value of this variable sparsely, using `gather`.

### `to_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/resource_variable_ops.py#L931-L975)

to_proto(
        export_scope=None
    )

Converts a `ResourceVariable` to a `VariableDef` protocol buffer.

|     |     |
| --- | --- |
| Args |     |
| `export_scope` | Optional `string`. Name scope to remove. |

|     |     |
| --- | --- |
| Raises |     |
| `RuntimeError` | If run in EAGER mode. |

|     |
| --- |
| Returns |     |
| A `VariableDef` protocol buffer, or `None` if the `Variable` is not in the specified name scope. |     |

### `value`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/resource_variable_ops.py#L653-L658)

value()

A cached operation which reads the value of this variable.

### `__abs__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/tensor_math_operator_overrides.py#L141-L144)

__abs__(
        name=None
    )

### `__add__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L105-L131)

__add__(
        y
    )

### `__and__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L105-L131)

__and__(
        y
    )

### `__array__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/resource_variable_ops.py#L559-L574)

__array__(
        dtype=None
    )

Allows direct conversion to a numpy array.

    np.array(tf.Variable([1.0]))

|     |
| --- |
| Returns |     |
| The variable value as a numpy array. |     |

### `__bool__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/resource_variable_ops.py#L579-L580)

__bool__()

### `__div__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L105-L131)

__div__(
        y
    )

### `__eq__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L1036-L1045)

__eq__(
        other
    )

Compares two variables element-wise for equality.

### `__floordiv__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L105-L131)

__floordiv__(
        y
    )

### `__ge__`

__ge__(
        y: Annotated[Any, tf.raw_ops.Any],
        name=None
    ) -> Annotated[Any, tf.raw_ops.Any]

Returns the truth value of (x >= y) element-wise.

#### Example:

x = tf.constant([5, 4, 6, 7])
    y = tf.constant([5, 2, 5, 10])
    tf.math.greater_equal(x, y) ==> [True, True, True, False]
    
    x = tf.constant([5, 4, 6, 7])
    y = tf.constant([5])
    tf.math.greater_equal(x, y) ==> [True, False, True, True]

|     |     |
| --- | --- |
| Args |     |
| `x` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns |     |
| A `Tensor` of type `bool`. |     |

### `__getitem__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/tensor_getitem_override.py#L270-L311)

__getitem__(
        slice_spec
    )

Creates a slice helper object given a variable.

This allows creating a sub-tensor from part of the current contents of a variable. See [`tf.Tensor.**getitem**`](https://www.tensorflow.org/api_docs/python/tf/Tensor#__getitem__)
 for detailed examples of slicing.

This function in addition also allows assignment to a sliced range. This is similar to `__setitem__` functionality in Python. However, the syntax is different so that the user can capture the assignment operation for grouping or passing to `sess.run()` in TF1. For example,

import tensorflow as tf
    A = tf.Variable([[1,2,3], [4,5,6], [7,8,9]], dtype=tf.float32)
    print(A[:2, :2])  # => [[1,2], [4,5]]
    
    A[:2,:2].assign(22. * tf.ones((2, 2))))
    print(A) # => [[22, 22, 3], [22, 22, 6], [7,8,9]]

Note that assignments currently do not support NumPy broadcasting semantics.

|     |     |
| --- | --- |
| Args |     |
| `var` | An `ops.Variable` object. |
| `slice_spec` | The arguments to [`Tensor.**getitem**`](https://www.tensorflow.org/api_docs/python/tf/Tensor#__getitem__)<br>. |

|     |
| --- |
| Returns |     |
| The appropriate slice of "tensor", based on "slice\_spec". As an operator. The operator also has a `assign()` method that can be used to generate an assignment operator. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If a slice range is negative size. |
| `TypeError` | TypeError: If the slice indices aren't int, slice, ellipsis, tf.newaxis or int32/int64 tensors. |

### `__gt__`

__gt__(
        y: Annotated[Any, tf.raw_ops.Any],
        name=None
    ) -> Annotated[Any, tf.raw_ops.Any]

Returns the truth value of (x > y) element-wise.

#### Example:

x = tf.constant([5, 4, 6])
    y = tf.constant([5, 2, 5])
    tf.math.greater(x, y) ==> [False, True, True]
    
    x = tf.constant([5, 4, 6])
    y = tf.constant([5])
    tf.math.greater(x, y) ==> [False, False, True]

|     |     |
| --- | --- |
| Args |     |
| `x` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns |     |
| A `Tensor` of type `bool`. |     |

### `__invert__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/tensor_math_operator_overrides.py#L135-L138)

__invert__(
        name=None
    )

### `__iter__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L1059-L1061)

__iter__()

When executing eagerly, iterates over the value of the variable.

### `__le__`

__le__(
        y: Annotated[Any, tf.raw_ops.Any],
        name=None
    ) -> Annotated[Any, tf.raw_ops.Any]

Returns the truth value of (x <= y) element-wise.

#### Example:

x = tf.constant([5, 4, 6])
    y = tf.constant([5])
    tf.math.less_equal(x, y) ==> [True, True, False]
    
    x = tf.constant([5, 4, 6])
    y = tf.constant([5, 6, 6])
    tf.math.less_equal(x, y) ==> [True, True, True]

|     |     |
| --- | --- |
| Args |     |
| `x` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns |     |
| A `Tensor` of type `bool`. |     |

### `__lt__`

__lt__(
        y: Annotated[Any, tf.raw_ops.Any],
        name=None
    ) -> Annotated[Any, tf.raw_ops.Any]

Returns the truth value of (x < y) element-wise.

#### Example:

x = tf.constant([5, 4, 6])
    y = tf.constant([5])
    tf.math.less(x, y) ==> [False, True, False]
    
    x = tf.constant([5, 4, 6])
    y = tf.constant([5, 6, 7])
    tf.math.less(x, y) ==> [False, True, True]

|     |     |
| --- | --- |
| Args |     |
| `x` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns |     |
| A `Tensor` of type `bool`. |     |

### `__matmul__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L105-L131)

__matmul__(
        y
    )

### `__mod__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L105-L131)

__mod__(
        y
    )

### `__mul__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L105-L131)

__mul__(
        y
    )

### `__ne__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L1048-L1057)

__ne__(
        other
    )

Compares two variables element-wise for equality.

### `__neg__`

__neg__(
        name=None
    ) -> Annotated[Any, tf.raw_ops.Any]

Computes numerical negative value element-wise.

I.e., y\=−x.

|     |     |
| --- | --- |
| Args |     |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int8`, `int16`, `int32`, `int64`, `complex64`, `complex128`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns |     |
| A `Tensor`. Has the same type as `x`. |     |

### `__nonzero__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/resource_variable_ops.py#L576-L577)

__nonzero__()

### `__or__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L105-L131)

__or__(
        y
    )

### `__pow__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L105-L131)

__pow__(
        y
    )

### `__radd__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L144-L150)

__radd__(
        x
    )

### `__rand__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L144-L150)

__rand__(
        x
    )

### `__rdiv__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L144-L150)

__rdiv__(
        x
    )

### `__rfloordiv__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L144-L150)

__rfloordiv__(
        x
    )

### `__rmatmul__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L144-L150)

__rmatmul__(
        x
    )

### `__rmod__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L144-L150)

__rmod__(
        x
    )

### `__rmul__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L144-L150)

__rmul__(
        x
    )

### `__ror__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L144-L150)

__ror__(
        x
    )

### `__rpow__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L144-L150)

__rpow__(
        x
    )

### `__rsub__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L144-L150)

__rsub__(
        x
    )

### `__rtruediv__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L144-L150)

__rtruediv__(
        x
    )

### `__rxor__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L144-L150)

__rxor__(
        x
    )

### `__sub__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L105-L131)

__sub__(
        y
    )

### `__truediv__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L105-L131)

__truediv__(
        y
    )

### `__xor__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/override_binary_operator.py#L105-L131)

__xor__(
        y
    )

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.