[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/train/experimental/ShardByTaskPolicy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/train/experimental/ShardByTaskPolicy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/train/experimental/ShardByTaskPolicy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/train/experimental/ShardByTaskPolicy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/train/experimental/ShardByTaskPolicy#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/train/experimental/ShardByTaskPolicy#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.train.experimental.ShardByTaskPolicy Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/train/experimental/ShardByTaskPolicy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/train/experimental/ShardByTaskPolicy#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/train/experimental/ShardByTaskPolicy#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/sharding/sharding_policies.py#L37-L68)

Policy that splits tensors into shards based on their device spec task.

Inherits From: [`ShardingCallback`](https://www.tensorflow.org/api_docs/python/tf/train/experimental/ShardingCallback)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.train.experimental.ShardByTaskPolicy`](https://www.tensorflow.org/api_docs/python/tf/train/experimental/ShardByTaskPolicy)

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `description` | Returns a text description of the sharding policy. |

Methods
-------

### `__call__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/sharding/sharding_policies.py#L45-L68)

__call__(
        shardable_tensors: Sequence[tf.train.experimental.ShardableTensor]
    ) -> Sequence[sharding_util.Shard]

Callback to split tensors into shards based on their device spec task.

|     |     |
| --- | --- |
| Args |     |
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