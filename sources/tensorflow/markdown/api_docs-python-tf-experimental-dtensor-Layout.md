[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#methods)
    *   [as\_proto](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#as_proto)
        
    *   [batch\_sharded](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#batch_sharded)
        
    *   [delete](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#delete)
        
    *   [from\_device](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#from_device)
        
    *   [from\_proto](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#from_proto)
        
    *   [from\_single\_device\_mesh](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#from_single_device_mesh)
        
    *   [from\_string](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#from_string)
        
    *   [global\_shape\_from\_local\_shape](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#global_shape_from_local_shape)
        
    *   [inner\_sharded](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#inner_sharded)
        
    *   [is\_batch\_parallel](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#is_batch_parallel)
        
    *   [is\_fully\_replicated](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#is_fully_replicated)
        
    *   [is\_single\_device](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#is_single_device)
        
    *   [local\_shape\_from\_global\_shape](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#local_shape_from_global_shape)
        
    *   [num\_shards](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#num_shards)
        
    *   [offset\_to\_shard](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#offset_to_shard)
        
    *   [offset\_tuple\_to\_global\_index](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#offset_tuple_to_global_index)
        
    *   [replicated](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#replicated)
        
    *   [to\_parted](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#to_parted)
        
    *   [to\_string](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#to_string)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#__eq__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.dtensor.Layout Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#methods)
    *   [as\_proto](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#as_proto)
        
    *   [batch\_sharded](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#batch_sharded)
        
    *   [delete](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#delete)
        
    *   [from\_device](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#from_device)
        
    *   [from\_proto](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#from_proto)
        
    *   [from\_single\_device\_mesh](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#from_single_device_mesh)
        
    *   [from\_string](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#from_string)
        
    *   [global\_shape\_from\_local\_shape](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#global_shape_from_local_shape)
        
    *   [inner\_sharded](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#inner_sharded)
        
    *   [is\_batch\_parallel](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#is_batch_parallel)
        
    *   [is\_fully\_replicated](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#is_fully_replicated)
        
    *   [is\_single\_device](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#is_single_device)
        
    *   [local\_shape\_from\_global\_shape](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#local_shape_from_global_shape)
        
    *   [num\_shards](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#num_shards)
        
    *   [offset\_to\_shard](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#offset_to_shard)
        
    *   [offset\_tuple\_to\_global\_index](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#offset_tuple_to_global_index)
        
    *   [replicated](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#replicated)
        
    *   [to\_parted](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#to_parted)
        
    *   [to\_string](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#to_string)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout#__eq__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/layout.py#L351-L550)

Represents the layout information of a DTensor.

tf.experimental.dtensor.Layout(
        sharding_specs: List[str],
        mesh: tf.experimental.dtensor.Mesh
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [DTensor concepts](https://www.tensorflow.org/guide/dtensor_overview)<br>    <br>*   [Distributed training with Core APIs and DTensor](https://www.tensorflow.org/guide/core/distribution) | *   [Distributed training with DTensors](https://www.tensorflow.org/tutorials/distribute/dtensor_ml_tutorial)<br>    <br>*   [Using DTensors with Keras](https://www.tensorflow.org/tutorials/distribute/dtensor_keras_tutorial) |

A layout describes how a distributed tensor is partitioned across a mesh (and thus across devices). For each axis of the tensor, the corresponding sharding spec indicates which dimension of the mesh it is sharded over. A special sharding spec `UNSHARDED` indicates that axis is replicated on all the devices of that mesh.

Refer to [DTensor Concepts](https://www.tensorflow.org/guide/dtensor_overview)
 for in depth discussion and examples.

For example, let's consider a 1-D mesh:

Mesh(["TPU:0", "TPU:1", "TPU:2", "TPU:3", "TPU:4", "TPU:5"], [("x", 6)])

This mesh arranges 6 TPU devices into a 1-D array. `Layout([UNSHARDED], mesh)` is a layout for rank-1 tensor which is replicated on the 6 devices.

For another example, let's consider a 2-D mesh:

Mesh(["TPU:0", "TPU:1", "TPU:2", "TPU:3", "TPU:4", "TPU:5"],
         [("x", 3), ("y", 2)])

This mesh arranges 6 TPU devices into a `3x2` 2-D array. `Layout(["x", UNSHARDED], mesh)` is a layout for rank-2 tensor whose first axis is sharded on mesh dimension "x" and the second axis is replicated. If we place `np.arange(6).reshape((3, 2))` using this layout, the individual components tensors would look like:

Device  |  Component
     TPU:0     [[0, 1]]
     TPU:1     [[0, 1]]
     TPU:2     [[2, 3]]
     TPU:3     [[2, 3]]
     TPU:4     [[4, 5]]
     TPU:5     [[4, 5]]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `sharding_specs` | List of sharding specifications, each corresponding to a tensor axis. Each specification (dim\_sharding) can either be a mesh dimension or the special value UNSHARDED. |
| `mesh` | A mesh configuration for the Tensor. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `mesh` |     |
| `rank` |     |
| `shape` |     |
| `sharding_specs` |     |
| `type` |     |

Methods
-------

### `as_proto`

as_proto()

as\_proto(self: tensorflow.python.\_pywrap\_dtensor\_device.Layout) -> tensorflow::dtensor::LayoutProto

Returns the LayoutProto protobuf message.

### `batch_sharded`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/layout.py#L462-L473)

@classmethod

Returns a layout sharded on batch dimension.

### `delete`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/layout.py#L476-L483)

delete(
        dims: List[int]
    ) -> 'Layout'

Returns the layout with the give dimensions deleted.

### `from_device`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/layout.py#L515-L518)

@classmethod

Constructs a single device layout from a single device mesh.

### `from_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/layout.py#L485-L488)

@classmethod

Creates an instance from a LayoutProto.

### `from_single_device_mesh`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/layout.py#L510-L513)

@classmethod

Constructs a single device layout from a single device mesh.

### `from_string`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/layout.py#L490-L493)

@classmethod

Creates an instance from a human-readable string.

### `global_shape_from_local_shape`

global_shape_from_local_shape()

global\_shape\_from\_local\_shape(self: tensorflow.python.\_pywrap\_dtensor\_device.Layout, local\_shape: list\[int\]) -> tuple

Returns the global shape computed from this local shape.

### `inner_sharded`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/layout.py#L505-L508)

@classmethod

Returns a layout sharded on inner dimension.

### `is_batch_parallel`

is_batch_parallel()

is\_batch\_parallel(self: tensorflow.python.\_pywrap\_dtensor\_device.Layout) -> bool

### `is_fully_replicated`

is_fully_replicated()

is\_fully\_replicated(self: tensorflow.python.\_pywrap\_dtensor\_device.Layout) -> bool

Returns True if all tensor axes are replicated.

### `is_single_device`

is_single_device()

is\_single\_device(self: tensorflow.python.\_pywrap\_dtensor\_device.Layout) -> bool

Returns True if the Layout represents a non-distributed device.

### `local_shape_from_global_shape`

local_shape_from_global_shape()

local\_shape\_from\_global\_shape(self: tensorflow.python.\_pywrap\_dtensor\_device.Layout, global\_shape: list\[int\]) -> tuple

Returns the local shape computed from this global shape.

### `num_shards`

num_shards()

num\_shards(self: tensorflow.python.\_pywrap\_dtensor\_device.Layout, idx: int) -> int

Returns the number of shards for tensor dimension `idx`.

### `offset_to_shard`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/layout.py#L521-L534)

offset_to_shard()

Mapping from offset in a flattened list to shard index.

### `offset_tuple_to_global_index`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/layout.py#L537-L545)

offset_tuple_to_global_index(
        offset_tuple
    )

Mapping from offset to index in global tensor.

### `replicated`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/layout.py#L547-L550)

@classmethod

Returns a replicated layout of rank `rank`.

### `to_parted`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/layout.py#L495-L503)

to_parted() -> 'Layout'

Returns a "parted" layout from a static layout.

A parted layout contains axes that are treated as independent by most of SPMD expanders.

FIXME(b/285905569): The exact semantics is still being investigated.

### `to_string`

to_string()

to\_string(self: tensorflow.python.\_pywrap\_dtensor\_device.Layout) -> str

### `__eq__`

__eq__()

**eq**(self: tensorflow.python.\_pywrap\_dtensor\_device.Layout, arg0: tensorflow.python.\_pywrap\_dtensor\_device.Layout) -> bool

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.