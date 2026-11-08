[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/replicate#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/replicate)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/replicate?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/replicate#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/replicate#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/replicate#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.tpu.replicate Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/replicate#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/replicate#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/replicate#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu.py#L270-L376)

Builds a graph operator that runs a replicated TPU computation.

tf.compat.v1.tpu.replicate(
        computation: Callable[..., Any],
        inputs: Optional[List[List[core_types.Tensor]]] = None,
        infeed_queue: Optional[tpu_feed.InfeedQueue] = None,
        device_assignment: Optional[tf.tpu.experimental.DeviceAssignment] = None,
        name: Optional[Text] = None,
        maximum_shapes: Optional[Any] = None,
        padding_spec: Optional[tf.compat.v1.tpu.PaddingSpec] = None,
        xla_options: Optional[tf.tpu.XLAOptions] = None
    ) -> List[Any]

Example for the basic usage that `inputs` has static shape:

def computation(x):
      x = x + 1
      return tf.math.reduce_mean(x)
    
    x = tf.convert_to_tensor([1., 2., 3.])
    y = tf.convert_to_tensor([4., 5., 6.])
    tf.compat.v1.tpu.replicate(computation, inputs=[[x], [y]])

If the `inputs` has dynamic shapes and you would like to automatically bucketize the inputs to avoid XLA recompilation. See the advanced example below:

def computation(x):
      x = x + 1
      return tf.math.reduce_mean(x)
    
    # Assume input tensors in two replicas `x` and `y` both have dynamic shape
    # ([None, 2]).
    tf.compat.v1.tpu.replicate(
      computation,
      inputs=[x, y],
      maximum_shapes=[tf.TensorShape([None, None])],
      padding_spec=tf.compat.v1.tpu.PaddingSpec.POWER_OF_TWO)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `computation` | A Python function that builds the computation to replicate. |
| `inputs` | A list of lists of input tensors or `None` (equivalent to `[[]]`), indexed by `[replica_num][input_num]`. All replicas must have the same number of inputs. Each input can be a nested structure containing values that are convertible to tensors. Note that passing an N-dimension list of compatible values will result in a N-dimension list of scalar tensors rather than a single Rank-N tensors. If you need different behavior, convert part of inputs to tensors with [`tf.convert_to_tensor`](https://www.tensorflow.org/api_docs/python/tf/convert_to_tensor)<br>. |
| `infeed_queue` | If not `None`, the `InfeedQueue` from which to append a tuple of arguments as inputs to computation. |
| `device_assignment` | If not `None`, a `DeviceAssignment` describing the mapping between logical cores in the computation with physical cores in the TPU topology. Uses a default device assignment if `None`. The `DeviceAssignment` may be omitted if each replica of the computation uses only one core, and there is either only one replica, or the number of replicas is equal to the number of cores in the TPU system. |
| `name` | (Deprecated) Does nothing. |
| `maximum_shapes` | A nested structure of tf.TensorShape representing the shape to which the respective component of each input element in each replica should be padded. Any unknown dimensions (e.g. tf.compat.v1.Dimension(None) in a tf.TensorShape or -1 in a tensor-like object) will be padded to the maximum size of that dimension over all replicas. The structure of `maximum_shapes` needs to be the same as `inputs[0]`. |
| `padding_spec` | An enum specified by `tpu.PaddingSpec`. This describes the padding policy when the `inputs` to `tpu.replicate` is dynamic. One usage is to enable automatic bucketizing on the inputs by setting the value to `tpu.PaddingSpec.POWER_OF_TWO`, which can help to reduce the recompilation in the XLA side. |
| `xla_options` | An instance of [`tpu.XLAOptions`](https://www.tensorflow.org/api_docs/python/tf/tpu/XLAOptions)<br> which indicates the options passed to XLA compiler. Use `None` for default options. |

|     |
| --- |
| Returns<br>------- |     |
| A list of outputs, indexed by `[replica_num]` each output can be a nested structure same as what computation() returns with a few exceptions.<br><br>Exceptions include:<br><br>1) None output: a NoOp would be returned which control-depends on computation. 2) Single value output: A tuple containing the value would be returned. 3) Operation-only outputs: a NoOp would be returned which control-depends on computation. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If all replicas do not have equal numbers of input tensors. |
| `ValueError` | If the number of inputs per replica does not match the number of formal parameters to `computation`. |
| `ValueError` | If the static `inputs` dimensions don't match with the values given in `maximum_shapes`. |
| `ValueError` | If the structure of inputs per replica does not match the structure of `maximum_shapes`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.