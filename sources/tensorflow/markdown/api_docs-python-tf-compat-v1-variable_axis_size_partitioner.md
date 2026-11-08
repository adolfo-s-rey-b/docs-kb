[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/variable_axis_size_partitioner#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.variable\_axis\_size\_partitioner Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/partitioned_variables.py#L67-L151)

Get a partitioner for VariableScope to keep shards below `max_shard_bytes`.

tf.compat.v1.variable_axis_size_partitioner(
        max_shard_bytes, axis=0, bytes_per_string_element=16, max_shards=None
    )

This partitioner will shard a Variable along one axis, attempting to keep the maximum shard size below `max_shard_bytes`. In practice, this is not always possible when sharding along only one axis. When this happens, this axis is sharded as much as possible (i.e., every dimension becomes a separate shard).

If the partitioner hits the `max_shards` limit, then each shard may end up larger than `max_shard_bytes`. By default `max_shards` equals `None` and no limit on the number of shards is enforced.

One reasonable value for `max_shard_bytes` is `(64 << 20) - 1`, or almost `64MB`, to keep below the protobuf byte limit.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `max_shard_bytes` | The maximum size any given shard is allowed to be. |
| `axis` | The axis to partition along. Default: outermost axis. |
| `bytes_per_string_element` | If the `Variable` is of type string, this provides an estimate of how large each scalar in the `Variable` is. |
| `max_shards` | The maximum number of shards in int created taking precedence over `max_shard_bytes`. |

|     |
| --- |
| Returns<br>------- |     |
| A partition function usable as the `partitioner` argument to `variable_scope` and `get_variable`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If any of the byte counts are non-positive. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.