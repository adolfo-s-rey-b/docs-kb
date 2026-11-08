[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/partitioners/MaxSizePartitioner#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/partitioners/MaxSizePartitioner)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/partitioners/MaxSizePartitioner?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/partitioners/MaxSizePartitioner#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/partitioners/MaxSizePartitioner#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/partitioners/MaxSizePartitioner#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.experimental.partitioners.MaxSizePartitioner Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/partitioners/MaxSizePartitioner#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/partitioners/MaxSizePartitioner#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/partitioners/MaxSizePartitioner#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/sharded_variable.py#L175-L239)

Partitioner that keeps shards below `max_shard_bytes`.

Inherits From: [`Partitioner`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/partitioners/Partitioner)

tf.distribute.experimental.partitioners.MaxSizePartitioner(
        max_shard_bytes, max_shards=None, bytes_per_string=16
    )

This partitioner ensures each shard has at most `max_shard_bytes`, and tries to allocate as few shards as possible, i.e., keeping shard size as large as possible.

If the partitioner hits the `max_shards` limit, then each shard may end up larger than `max_shard_bytes`. By default `max_shards` equals `None` and no limit on the number of shards is enforced.

#### Examples:

    partitioner = MaxSizePartitioner(max_shard_bytes=4)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `max_shard_bytes` | The maximum size any given shard is allowed to be. |
| `max_shards` | The maximum number of shards in `int` created taking precedence over `max_shard_bytes`. |
| `bytes_per_string` | If the partition value is of type string, this provides an estimate of how large each string is. |

Methods
-------

### `__call__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/sharded_variable.py#L233-L239)

__call__(
        shape, dtype, axis=0
    )

Partitions the given `shape` and returns the partition results.

Examples of a partitioner that allocates a fixed number of shards:

partitioner = FixedShardsPartitioner(num_shards=2)
    partitions = partitioner(tf.TensorShape([10, 3], tf.float32), axis=0)
    print(partitions) # [2, 0]

|     |     |
| --- | --- |
| Args |     |
| `shape` | a [`tf.TensorShape`](https://www.tensorflow.org/api_docs/python/tf/TensorShape)<br>, the shape to partition. |
| `dtype` | a `tf.dtypes.Dtype` indicating the type of the partition value. |
| `axis` | The axis to partition along. Default: outermost axis. |

|     |
| --- |
| Returns |     |
| A list of integers representing the number of partitions on each axis, where i-th value corresponds to i-th axis. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.