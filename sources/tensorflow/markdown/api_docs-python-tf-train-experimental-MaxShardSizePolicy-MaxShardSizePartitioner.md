[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/train/experimental/MaxShardSizePolicy/MaxShardSizePartitioner#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/train/experimental/MaxShardSizePolicy/MaxShardSizePartitioner)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/train/experimental/MaxShardSizePolicy/MaxShardSizePartitioner?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/train/experimental/MaxShardSizePolicy/MaxShardSizePartitioner#methods)
    *   [get\_shards](https://www.tensorflow.org/api_docs/python/tf/train/experimental/MaxShardSizePolicy/MaxShardSizePartitioner#get_shards)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.train.experimental.MaxShardSizePolicy.MaxShardSizePartitioner Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/train/experimental/MaxShardSizePolicy/MaxShardSizePartitioner#methods)
    *   [get\_shards](https://www.tensorflow.org/api_docs/python/tf/train/experimental/MaxShardSizePolicy/MaxShardSizePartitioner#get_shards)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/sharding/sharding_policies.py#L83-L340)

Partition tensors into shards with a max shard size.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.train.experimental.MaxShardSizePolicy.MaxShardSizePartitioner`](https://www.tensorflow.org/api_docs/python/tf/train/experimental/MaxShardSizePolicy/MaxShardSizePartitioner)

Methods
-------

### `get_shards`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/sharding/sharding_policies.py#L190-L340)

get_shards(
        max_shard_size: int,
        shardable_tensors: Sequence[tf.train.experimental.ShardableTensor]
    ) -> Sequence[sharding_util.Shard]

Callback to split tensors into shards with a max shard size.

|     |     |
| --- | --- |
| Args |     |
| `max_shard_size` | The maximum size of a shard file in bytes. |
| `shardable_tensors` | A list of ShardableTensors. |

|     |
| --- |
| Returns |     |
| List of shard dicts containing tensors. \[ {checkpoint key: {slice\_spec: tensor} } \] |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.