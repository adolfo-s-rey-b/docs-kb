[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/batch_parallel#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/batch_parallel)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/batch_parallel?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/batch_parallel#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/batch_parallel#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/batch_parallel#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.tpu.batch\_parallel Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/batch_parallel#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/batch_parallel#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/batch_parallel#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu.py#L1379-L1439)

Shards `computation` along the batch dimension for parallel execution.

tf.compat.v1.tpu.batch_parallel(
        computation: Callable[..., Any],
        inputs: Optional[List[List[Optional[core_types.Tensor]]]] = None,
        num_shards: int = 1,
        infeed_queue: Optional[tpu_feed.InfeedQueue] = None,
        device_assignment: Optional[tf.tpu.experimental.DeviceAssignment] = None,
        name: Optional[Text] = None,
        xla_options: Optional[tf.tpu.XLAOptions] = None
    )

Convenience wrapper around shard().

`inputs` must be a list of Tensors or None (equivalent to an empty list). Each input is split into `num_shards` pieces along the 0-th dimension, and computation is applied to each shard in parallel.

Tensors are broadcast to all shards if they are lexically captured by `computation`. e.g.,

x = tf.constant(7) def computation(): return x + 3 ... = shard(computation, ...)

The outputs from all shards are concatenated back together along their 0-th dimension.

Inputs and outputs of the computation must be at least rank-1 Tensors.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `computation` | A Python function that builds a computation to apply to each shard of the input. |
| `inputs` | A list of input tensors or None (equivalent to an empty list). The 0-th dimension of each Tensor must have size divisible by `num_shards`. |
| `num_shards` | The number of shards. |
| `infeed_queue` | If not `None`, the `InfeedQueue` from which to append a tuple of arguments as inputs to `computation`. |
| `device_assignment` | If not `None`, a `DeviceAssignment` describing the mapping between logical cores in the computation with physical cores in the TPU topology. Uses a default device assignment if `None`. The `DeviceAssignment` may be omitted if each shard of the computation uses only one core, and there is either only one shard, or the number of shards is equal to the number of cores in the TPU system. |
| `name` | (Deprecated) Does nothing. |
| `xla_options` | An instance of [`tpu.XLAOptions`](https://www.tensorflow.org/api_docs/python/tf/tpu/XLAOptions)<br> which indicates the options passed to XLA compiler. Use `None` for default options. |

|     |
| --- |
| Returns<br>------- |     |
| A list of output tensors. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `num_shards <= 0` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.