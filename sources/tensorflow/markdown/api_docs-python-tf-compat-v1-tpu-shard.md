[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/shard#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/shard)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/shard?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Ftpu%2Fshard&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/shard#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/shard#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/shard#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.tpu.shard Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/shard#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/shard#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/shard#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu.py#L1292-L1376)

Shards `computation` for parallel execution.

tf.compat.v1.tpu.shard(
        computation: Callable[..., Any],
        inputs: Optional[List[core_types.Tensor]] = None,
        num_shards: int = 1,
        input_shard_axes: Optional[List[int]] = None,
        outputs_from_all_shards: Union[bool, List[bool]] = True,
        output_shard_axes: Optional[List[int]] = None,
        infeed_queue: Optional[tpu_feed.InfeedQueue] = None,
        device_assignment: Optional[tf.tpu.experimental.DeviceAssignment] = None,
        name: Optional[Text] = None,
        xla_options: Optional[tf.tpu.XLAOptions] = None
    ) -> List[core_types.Tensor]

`inputs` must be a list of Tensors or None (equivalent to an empty list), each of which has a corresponding split axis (from `input_shard_axes`). Each input is split into `num_shards` pieces along the corresponding axis, and computation is applied to each shard in parallel.

Tensors are broadcast to all shards if they are lexically captured by `computation`. e.g.,

x = tf.constant(7) def computation(): return x + 3 ... = shard(computation, ...)

as inputs.

If `outputs_from_all_shards` is true, the outputs from all shards of `computation` are concatenated back together along their `output_shard_axes`. Otherwise, each output is taken from an arbitrary shard.

Inputs and outputs of the computation must be at least rank-1 Tensors.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `computation` | A Python function that builds a computation to apply to each shard of the input. |
| `inputs` | A list of input tensors or None (equivalent to an empty list). Each input tensor has a corresponding shard axes, given by `input_shard_axes`, which must have size divisible by `num_shards`. |
| `num_shards` | The number of shards. |
| `input_shard_axes` | A list of dimensions along which to shard `inputs`, or `None`. `None` means "shard all inputs along dimension 0". If not `None`, there must be one dimension per input. |
| `outputs_from_all_shards` | Boolean or list of boolean. For each output, if `True`, outputs from all shards are concatenated along the corresponding `output_shard_axes` entry. Otherwise, each output is taken from an arbitrary shard. If the argument is a boolean, the argument's value is used for each output. |
| `output_shard_axes` | A list of dimensions along which to concatenate the outputs of `computation`, or `None`. `None` means "concatenate all outputs along dimension 0". If not `None`, there must be one dimension per output. Ignored if `outputs_from_all_shards` is False. |
| `infeed_queue` | If not `None`, the `InfeedQueue` to use to augment the inputs of `computation`. |
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
| `ValueError` | If num\_shards <= 0 |
| `ValueError` | If len(input\_shard\_axes) != len(inputs) |
| `ValueError` | If len(output\_shard\_axes) != len(outputs from `computation`) |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.