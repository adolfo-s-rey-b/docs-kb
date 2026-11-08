[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/train/experimental/ShardingCallback#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/train/experimental/ShardingCallback)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/train/experimental/ShardingCallback?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/train/experimental/ShardingCallback#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/train/experimental/ShardingCallback#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/train/experimental/ShardingCallback#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.train.experimental.ShardingCallback Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/train/experimental/ShardingCallback#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/train/experimental/ShardingCallback#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/train/experimental/ShardingCallback#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/sharding/sharding_util.py#L76-L162)

Checkpoint sharding callback function, along with a text description.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.train.experimental.ShardingCallback`](https://www.tensorflow.org/api_docs/python/tf/train/experimental/ShardingCallback)

A callback function wrapper that will be executed to determine how tensors will be split into shards when the saver writes the checkpoint shards to disk.

The callback takes a list of [`tf.train.experimental.ShardableTensor`](https://www.tensorflow.org/api_docs/python/tf/train/experimental/ShardableTensor)
s as input (as well as any kwargs defined by the [`tf.train.experimental.ShardingCallback`](https://www.tensorflow.org/api_docs/python/tf/train/experimental/ShardingCallback)
 subclass), and organizes the input tensors into different shards. Tensors are first organized by device task (see [`tf.DeviceSpec`](https://www.tensorflow.org/api_docs/python/tf/DeviceSpec)
), then the callback will be called for each collection of tensors.

There are a few restrictions to keep in mind when creating a custom callback:

*   Tensors must not be removed from the checkpoint.
*   Tensors must not be reshaped.
*   Tensor dtypes must not change.
*   Tensors within a shard must belong to the same task. Validation checks will be performed after the callback function is executed to ensure these restrictions aren't violated.

Here's an example of a simple custom callback:

# Place all tensors in a single shard.
    class AllInOnePolicy(tf.train.experimental.ShardingCallback):
      @property
      def description(self):
        return "Place all tensors in a single shard."
    
      def __call__(self, shardable_tensors):
        tensors = {}
        for shardable_tensor in shardable_tensors:
          tensor = shardable_tensor.tensor_save_spec.tensor
          checkpoint_key = shardable_tensor.checkpoint_key
          slice_spec = shardable_tensor.slice_spec
    
          tensors.set_default(checkpoint_key, {})[slice_spec] = tensor
        return [tensors]
    
    ckpt.save(
        "path",
        options=tf.train.CheckpointOptions(
            experimental_sharding_callback=AllInOnePolicy()))

The `description` attribute is used to identify the callback and to aid debugging during saving and restoration.

To take in kwargs, simply define the constructor and pass them in:

class ParameterPolicy(tf.train.experimental.ShardingCallback):
      def __init__(self, custom_param):
        self.custom_param = custom_param
      ...
    
    ckpt.save(
        "path",
        options=tf.train.CheckpointOptions(
            experimental_sharding_callback=ParameterPolicy(custom_param=...)))

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `description` | Returns a text description of the sharding policy. |

Methods
-------

### `__call__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/sharding/sharding_util.py#L147-L152)

@abc.abstractmethod

Returns a list of shards for the given shardable tensors.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.