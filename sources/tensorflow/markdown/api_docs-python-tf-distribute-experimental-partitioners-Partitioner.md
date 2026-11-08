[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/partitioners/Partitioner#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/partitioners/Partitioner)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/partitioners/Partitioner?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/partitioners/Partitioner#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/partitioners/Partitioner#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.experimental.partitioners.Partitioner Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/partitioners/Partitioner#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/partitioners/Partitioner#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/sharded_variable.py#L46-L80)

Partitioner base class: all partitiners inherit from this class.

Partitioners should implement a `__call__` method with the following signature:

def __call__(self, shape, dtype, axis=0):
      # Partitions the given `shape` and returns the partition results.
      # See docstring of `__call__` method for the format of partition results.

Methods
-------

### `__call__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/sharded_variable.py#L60-L80)

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