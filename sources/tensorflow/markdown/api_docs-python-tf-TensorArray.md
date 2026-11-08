[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/TensorArray#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/TensorArray)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/TensorArray?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/TensorArray#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/TensorArray#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/TensorArray#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/TensorArray#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/TensorArray#methods)
    *   [close](https://www.tensorflow.org/api_docs/python/tf/TensorArray#close)
        
    *   [concat](https://www.tensorflow.org/api_docs/python/tf/TensorArray#concat)
        
    *   [gather](https://www.tensorflow.org/api_docs/python/tf/TensorArray#gather)
        
    *   [grad](https://www.tensorflow.org/api_docs/python/tf/TensorArray#grad)
        
    *   [identity](https://www.tensorflow.org/api_docs/python/tf/TensorArray#identity)
        
    *   [read](https://www.tensorflow.org/api_docs/python/tf/TensorArray#read)
        
    *   [scatter](https://www.tensorflow.org/api_docs/python/tf/TensorArray#scatter)
        
    *   [size](https://www.tensorflow.org/api_docs/python/tf/TensorArray#size)
        
    *   [split](https://www.tensorflow.org/api_docs/python/tf/TensorArray#split)
        
    *   [stack](https://www.tensorflow.org/api_docs/python/tf/TensorArray#stack)
        
    *   [unstack](https://www.tensorflow.org/api_docs/python/tf/TensorArray#unstack)
        
    *   [write](https://www.tensorflow.org/api_docs/python/tf/TensorArray#write)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.TensorArray Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/TensorArray#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/TensorArray#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/TensorArray#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/TensorArray#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/TensorArray#methods)
    *   [close](https://www.tensorflow.org/api_docs/python/tf/TensorArray#close)
        
    *   [concat](https://www.tensorflow.org/api_docs/python/tf/TensorArray#concat)
        
    *   [gather](https://www.tensorflow.org/api_docs/python/tf/TensorArray#gather)
        
    *   [grad](https://www.tensorflow.org/api_docs/python/tf/TensorArray#grad)
        
    *   [identity](https://www.tensorflow.org/api_docs/python/tf/TensorArray#identity)
        
    *   [read](https://www.tensorflow.org/api_docs/python/tf/TensorArray#read)
        
    *   [scatter](https://www.tensorflow.org/api_docs/python/tf/TensorArray#scatter)
        
    *   [size](https://www.tensorflow.org/api_docs/python/tf/TensorArray#size)
        
    *   [split](https://www.tensorflow.org/api_docs/python/tf/TensorArray#split)
        
    *   [stack](https://www.tensorflow.org/api_docs/python/tf/TensorArray#stack)
        
    *   [unstack](https://www.tensorflow.org/api_docs/python/tf/TensorArray#unstack)
        
    *   [write](https://www.tensorflow.org/api_docs/python/tf/TensorArray#write)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/tensor_array_ops.py#L971-L1317)

Class wrapping dynamic-sized, per-time-step, Tensor arrays.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.TensorArray`](https://www.tensorflow.org/api_docs/python/tf/TensorArray)

tf.TensorArray(
        dtype,
        size=None,
        dynamic_size=None,
        clear_after_read=None,
        tensor_array_name=None,
        handle=None,
        flow=None,
        infer_shape=True,
        element_shape=None,
        colocate_with_first_write_call=True,
        name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Effective Tensorflow 2](https://www.tensorflow.org/guide/effective_tf2)<br>    <br>*   [Better performance with tf.function](https://www.tensorflow.org/guide/function) | *   [Playing CartPole with the Actor-Critic method](https://www.tensorflow.org/tutorials/reinforcement_learning/actor_critic)<br>    <br>*   [Modeling COVID-19 spread in Europe and the effect of interventions](https://www.tensorflow.org/probability/examples/Estimating_COVID_19_in_11_European_countries)<br>    <br>*   [Neural machine translation with attention](https://www.tensorflow.org/text/tutorials/nmt_with_attention)<br>    <br>*   [Neural machine translation with a Transformer and Keras](https://www.tensorflow.org/text/tutorials/transformer) |

This class is meant to be used with dynamic iteration primitives such as `while_loop` and `map_fn`. It supports gradient back-propagation via special "flow" control flow dependencies.

Note that although the array can be read multiple times and positions can be overwritten, behavior may be undefined when storing multiple references to the same array and clear\_after\_read is False. In particular, avoid using methods like concat() to convert an intermediate TensorArray to a Tensor, then further modifying the TensorArray, particularly if you need to backprop through it later.

Example 1: Plain reading and writing.

    ta = tf.TensorArray(tf.float32, size=0, dynamic_size=True, clear_after_read=False)

Example 2: Fibonacci sequence algorithm that writes in a loop then returns.

    @tf.function

Example 3: A simple loop interacting with a [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
.

    v = tf.Variable(1)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `dtype` | (required) data type of the TensorArray. |
| `size` | (optional) int32 scalar `Tensor`: the size of the TensorArray. Required if handle is not provided. |
| `dynamic_size` | (optional) Python bool: If true, writes to the TensorArray can grow the TensorArray past its initial size. Default: False. |
| `clear_after_read` | Boolean (optional, default: True). If True, clear TensorArray values after reading them. This disables read-many semantics, but allows early release of memory. |
| `tensor_array_name` | (optional) Python string: the name of the TensorArray. This is used when creating the TensorArray handle. If this value is set, handle should be None. |
| `handle` | (optional) A `Tensor` handle to an existing TensorArray. If this is set, tensor\_array\_name should be None. Only supported in graph mode. |
| `flow` | (optional) A float `Tensor` scalar coming from an existing [`TensorArray.flow`](https://www.tensorflow.org/api_docs/python/tf/TensorArray#flow)<br>. Only supported in graph mode. |
| `infer_shape` | (optional, default: True) If True, shape inference is enabled. In this case, all elements must have the same shape. |
| `element_shape` | (optional, default: None) A `TensorShape` object specifying the shape constraints of each of the elements of the TensorArray. Need not be fully defined. |
| `colocate_with_first_write_call` | If `True`, the TensorArray will be colocated on the same device as the Tensor used on its first write (write operations include `write`, `unstack`, and `split`). If `False`, the TensorArray will be placed on the device determined by the device context available during its initialization. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if both handle and tensor\_array\_name are provided. |
| `TypeError` | if handle is provided but is not a Tensor. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `dtype` | The data type of this TensorArray. |
| `dynamic_size` | Python bool; if `True` the TensorArray can grow dynamically. |
| `element_shape` | The [`tf.TensorShape`](https://www.tensorflow.org/api_docs/python/tf/TensorShape)<br> of elements in this TensorArray. |
| `flow` | The flow `Tensor` forcing ops leading to this TensorArray state. |
| `handle` | The reference to the TensorArray. |

Methods
-------

### `close`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/tensor_array_ops.py#L1311-L1314)

close(
        name=None
    )

Close the current TensorArray.

### `concat`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/tensor_array_ops.py#L1235-L1247)

concat(
        name=None
    )

Return the values in the TensorArray as a concatenated `Tensor`.

All of the values must have been written, their ranks must match, and and their shapes must all match for all dimensions except the first.

|     |     |
| --- | --- |
| Args |     |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns |     |
| All the tensors in the TensorArray concatenated into one tensor. |     |

### `gather`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/tensor_array_ops.py#L1218-L1233)

gather(
        indices, name=None
    )

Return selected values in the TensorArray as a packed `Tensor`.

All of selected values must have been written and their shapes must all match.

|     |     |
| --- | --- |
| Args |     |
| `indices` | A `1-D` `Tensor` taking values in `[0, max_value)`. If the `TensorArray` is not dynamic, `max_value=size()`. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| The tensors in the `TensorArray` selected by `indices`, packed into one tensor. |     |\
\
### `grad`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/tensor_array_ops.py#L1157-L1158)\
\
grad(\
        source, flow=None, name=None\
    )\
\
### `identity`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/tensor_array_ops.py#L1147-L1155)\
\
identity()\
\
Returns a TensorArray with the same content and properties.\
\
|     |\
| --- |\
| Returns |     |\
| A new TensorArray object with flow that ensures the control dependencies from the contexts will become control dependencies for writes, reads, etc. Use this object for all subsequent operations. |     |\
\
### `read`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/tensor_array_ops.py#L1160-L1170)\
\
read(\
        index, name=None\
    )\
\
Read the value at location `index` in the TensorArray.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `index` | 0-D. int32 tensor with the index to read from. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| The tensor at index `index`. |     |\
\
### `scatter`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/tensor_array_ops.py#L1269-L1286)\
\
scatter(\
        indices, value, name=None\
    )\
\
Scatter the values of a `Tensor` in specific indices of a `TensorArray`.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `indices` | A `1-D` `Tensor` taking values in `[0, max_value)`. If the `TensorArray` is not dynamic, `max_value=size()`. |\
| `value` | (N+1)-D. Tensor of type `dtype`. The Tensor to unpack. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A new TensorArray object with flow that ensures the scatter occurs. Use this object for all subsequent operations. |     |\
\
|     |     |\
| --- | --- |\
| Raises |     |\
| `ValueError` | if the shape inference fails. |\
\
### `size`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/tensor_array_ops.py#L1307-L1309)\
\
size(\
        name=None\
    )\
\
Return the size of the TensorArray.\
\
### `split`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/tensor_array_ops.py#L1288-L1305)\
\
split(\
        value, lengths, name=None\
    )\
\
Split the values of a `Tensor` into the TensorArray.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `value` | (N+1)-D. Tensor of type `dtype`. The Tensor to split. |\
| `lengths` | 1-D. int32 vector with the lengths to use when splitting `value` along its first dimension. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A new TensorArray object with flow that ensures the split occurs. Use this object for all subsequent operations. |     |\
\
|     |     |\
| --- | --- |\
| Raises |     |\
| `ValueError` | if the shape inference fails. |\
\
### `stack`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/tensor_array_ops.py#L1190-L1216)\
\
stack(\
        name=None\
    )\
\
Return the values in the TensorArray as a stacked `Tensor`.\
\
All of the values must have been written and their shapes must all match. If input shapes have rank-`R`, then output shape will have rank-`(R+1)`.\
\
#### For example:\
\
    ta = tf.TensorArray(tf.int32, size=3)\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| All the tensors in the TensorArray stacked into one tensor. |     |\
\
### `unstack`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/tensor_array_ops.py#L1249-L1267)\
\
unstack(\
        value, name=None\
    )\
\
Unstack the values of a `Tensor` in the TensorArray.\
\
If input value shapes have rank-`R`, then the output TensorArray will contain elements whose shapes are rank-`(R-1)`.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `value` | (N+1)-D. Tensor of type `dtype`. The Tensor to unstack. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A new TensorArray object with flow that ensures the unstack occurs. Use this object for all subsequent operations. |     |\
\
|     |     |\
| --- | --- |\
| Raises |     |\
| `ValueError` | if the shape inference fails. |\
\
### `write`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/tensor_array_ops.py#L1172-L1188)\
\
write(\
        index, value, name=None\
    )\
\
Write `value` into index `index` of the TensorArray.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `index` | 0-D. int32 scalar with the index to write to. |\
| `value` | N-D. Tensor of type `dtype`. The Tensor to write to this index. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns |     |\
| A new TensorArray object with flow that ensures the write occurs. Use this object for all subsequent operations. |     |\
\
|     |     |\
| --- | --- |\
| Raises |     |\
| `ValueError` | if there are more writers than specified. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.