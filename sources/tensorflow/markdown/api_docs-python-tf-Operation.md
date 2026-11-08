[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/Operation#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/Operation)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/Operation?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2FOperation&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/Operation#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/Operation#methods)
    *   [colocation\_groups](https://www.tensorflow.org/api_docs/python/tf/Operation#colocation_groups)
        
    *   [experimental\_set\_type](https://www.tensorflow.org/api_docs/python/tf/Operation#experimental_set_type)
        
    *   [from\_node\_def](https://www.tensorflow.org/api_docs/python/tf/Operation#from_node_def)
        
    *   [get\_attr](https://www.tensorflow.org/api_docs/python/tf/Operation#get_attr)
        
    *   [run](https://www.tensorflow.org/api_docs/python/tf/Operation#run)
        
    *   [values](https://www.tensorflow.org/api_docs/python/tf/Operation#values)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Was this helpful?

tf.Operation Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/Operation#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/Operation#methods)
    *   [colocation\_groups](https://www.tensorflow.org/api_docs/python/tf/Operation#colocation_groups)
        
    *   [experimental\_set\_type](https://www.tensorflow.org/api_docs/python/tf/Operation#experimental_set_type)
        
    *   [from\_node\_def](https://www.tensorflow.org/api_docs/python/tf/Operation#from_node_def)
        
    *   [get\_attr](https://www.tensorflow.org/api_docs/python/tf/Operation#get_attr)
        
    *   [run](https://www.tensorflow.org/api_docs/python/tf/Operation#run)
        
    *   [values](https://www.tensorflow.org/api_docs/python/tf/Operation#values)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/ops.py#L1093-L1691)

Represents a graph node that performs computation on tensors.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.Operation`](https://www.tensorflow.org/api_docs/python/tf/Operation)

tf.Operation(
        *args, **kwargs
    )

An `Operation` is a node in a [`tf.Graph`](https://www.tensorflow.org/api_docs/python/tf/Graph)
 that takes zero or more `Tensor` objects as input, and produces zero or more `Tensor` objects as output. Objects of type `Operation` are created by calling a Python op constructor (such as [`tf.matmul`](https://www.tensorflow.org/api_docs/python/tf/linalg/matmul)
) within a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 or under a [`tf.Graph.as_default`](https://www.tensorflow.org/api_docs/python/tf/Graph#as_default)
 context manager.

For example, within a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
, `c = tf.matmul(a, b)` creates an `Operation` of type "MatMul" that takes tensors `a` and `b` as input, and produces `c` as output.

If a [`tf.compat.v1.Session`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Session)
 is used, an `Operation` of a [`tf.Graph`](https://www.tensorflow.org/api_docs/python/tf/Graph)
 can be executed by passing it to `tf.Session.run`. `op.run()` is a shortcut for calling `tf.compat.v1.get_default_session().run(op)`.

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `control_inputs` | The `Operation` objects on which this op has a control dependency.<br><br>Before this op is executed, TensorFlow will ensure that the operations in `self.control_inputs` have finished executing. This mechanism can be used to run ops sequentially for performance reasons, or to ensure that the side effects of an op are observed in the correct order. |
| `device` | The name of the device to which this op has been assigned, if any. |
| `graph` |     |
| `inputs` | The sequence of `Tensor` objects representing the data inputs of this op. |
| `name` |     |
| `node_def` |     |
| `op_def` |     |
| `outputs` |     |
| `traceback` | Returns the call stack from when this operation was constructed. |
| `type` |     |

Methods
-------

### `colocation_groups`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/ops.py#L1295-L1312)

colocation_groups() -> list[bytes]

Returns the list of colocation groups of the op.

### `experimental_set_type`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/ops.py#L1656-L1673)

experimental_set_type(
        type_proto
    ) -> None

Sets the corresponding node's `experimental_type` field.

See the description of `NodeDef.experimental_type` for more info.

|     |     |
| --- | --- |
| Args |     |
| `type_proto` | A FullTypeDef proto message. The root type\_if of this object must be `TFT_PRODUCT`, even for ops which only have a singlre return value. |

### `from_node_def`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/ops.py#L1112-L1230)

@classmethod

Creates an `Operation`.

[A-Za-z0-9.][A-Za-z0-9_.\\-/]*

|     |     |
| --- | --- |
| Args |     |
| `node_def` | `node_def_pb2.NodeDef`. `NodeDef` for the `Operation`. Used for attributes of `node_def_pb2.NodeDef`, typically `name`, `op`, and `device`. The `input` attribute is irrelevant here as it will be computed when generating the model. |
| `g` | `Graph`. The parent graph. |
| `inputs` | list of `Tensor` objects. The inputs to this `Operation`. |
| `output_types` | list of `DType` objects. List of the types of the `Tensors` computed by this operation. The length of this list indicates the number of output endpoints of the `Operation`. |
| `control_inputs` | list of operations or tensors from which to have a control dependency. |
| `input_types` | List of `DType` objects representing the types of the tensors accepted by the `Operation`. By default uses `[x.dtype.base_dtype for x in inputs]`. Operations that expect reference-typed inputs must specify these explicitly. |
| `original_op` | Optional. Used to associate the new `Operation` with an existing `Operation` (for example, a replica with the op that was replicated). |
| `op_def` | Optional. The `op_def_pb2.OpDef` proto that describes the op type that this `Operation` represents. |

|     |     |
| --- | --- |
| Raises |     |
| `TypeError` | if control inputs are not Operations or Tensors, or if `node_def` is not a `NodeDef`, or if `g` is not a `Graph`, or if `inputs` are not tensors, or if `inputs` and `input_types` are incompatible. |
| `ValueError` | if the `node_def` name is not valid. |

|     |
| --- |
| Returns |     |
| Operation object. |     |

### `get_attr`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/ops.py#L1592-L1629)

get_attr(
        name
    )

Returns the value of the attr of this op with the given `name`.

|     |     |
| --- | --- |
| Args |     |
| `name` | The name of the attr to fetch. |

|     |
| --- |
| Returns |     |
| The value of the attr, as a Python object. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If this op does not have an attr with the given `name`. |

### `run`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/ops.py#L1675-L1691)

run(
        feed_dict=None, session=None
    ) -> None

Runs this operation in a `Session`.

Calling this method will execute all preceding operations that produce the inputs needed for this operation.

|     |     |
| --- | --- |
| Args |     |
| `feed_dict` | A dictionary that maps `Tensor` objects to feed values. See `tf.Session.run` for a description of the valid feed values. |
| `session` | (Optional.) The `Session` to be used to run to this operation. If none, the default session will be used. |

### `values`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/ops.py#L1314-L1316)

values() -> tuple[Any, ...]

Was this helpful?

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.