[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/train/experimental/MaxShardSizePolicy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/train/experimental/MaxShardSizePolicy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/train/experimental/MaxShardSizePolicy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/train/experimental/MaxShardSizePolicy#attributes)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/train/experimental/MaxShardSizePolicy#child_classes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/train/experimental/MaxShardSizePolicy#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/train/experimental/MaxShardSizePolicy#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.train.experimental.MaxShardSizePolicy Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/train/experimental/MaxShardSizePolicy#attributes)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/train/experimental/MaxShardSizePolicy#child_classes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/train/experimental/MaxShardSizePolicy#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/train/experimental/MaxShardSizePolicy#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/sharding/sharding_policies.py#L74-L353)

Policy that splits tensors into shards with a max shard size.

Inherits From: [`ShardingCallback`](https://www.tensorflow.org/api_docs/python/tf/train/experimental/ShardingCallback)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.train.experimental.MaxShardSizePolicy`](https://www.tensorflow.org/api_docs/python/tf/train/experimental/MaxShardSizePolicy)

tf.train.experimental.MaxShardSizePolicy(
        max_shard_size: int
    )

Shards may exceed the max shard size if they contain 1. a single scalar/string tensor that could not be sliced and exceeds the max shard size or 2. the checkpoint object graph, whose size cannot be calculated when saving.

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `description` | Returns a text description of the sharding policy. |

Child Classes
-------------

[`class MaxShardSizePartitioner`](https://www.tensorflow.org/api_docs/python/tf/train/experimental/MaxShardSizePolicy/MaxShardSizePartitioner)

Methods
-------

### `__call__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/sharding/sharding_policies.py#L349-L353)

__call__(
        shardable_tensors: Sequence[tf.train.experimental.ShardableTensor]
    ) -> Sequence[sharding_util.Shard]

Returns a list of shards for the given shardable tensors.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.