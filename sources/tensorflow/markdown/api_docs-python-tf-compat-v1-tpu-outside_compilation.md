[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/outside_compilation#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/outside_compilation)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/outside_compilation?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/outside_compilation#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/outside_compilation#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.tpu.outside\_compilation Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/outside_compilation#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/outside_compilation#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_replication.py#L654-L719)

Builds part of a computation outside any current TPU replicate scope.

tf.compat.v1.tpu.outside_compilation(
        computation: Callable[..., Any], *args, **kwargs
    ) -> Any

`tf.tpu.outside_compilation()` is used to run ops in `computation` on CPU instead of running on TPU. For example, users can run ops that are not supported on TPU's (e.g. tf.summary.write()) by explicitly placing those ops on CPU's. Below usage of outside compilation will place ops in `computation_with_string_ops` on CPU.

#### Example usage:

def computation_with_string_ops(x):
      # strings types are not supported on TPU's and below ops must
      # run on CPU instead.
      output = tf.strings.format('1{}', x)
      return tf.strings.to_number(output)
    
    def tpu_computation():
      # Expected output is 11.
      output = tf.tpu.outside_compilation(computation_with_string_ops, 1)

Outside compilation should be called inside TPUReplicateContext. That is, `tf.tpu.outside_compilation()` should be called inside a function that is passed to `tpu.split_compile_and_replicate()` -- this is implied when outside compilation is invoked inside a function passed to TPUStrategy `run()`. If invoked outside of TPUReplicateContext, then this simply returns the result of `computation`, and therefore, would be a no-op. Note that outside compilation is different from `tf.distribute.experimental.TPUStrategy.merge_call()` as logic in outside compilation is replicated and executed separately for each replica. On the other hand, `merge_call()` requires a `merge_fn` to aggregate the inputs from different replicas and is executed only once.

For variables placed in TPU device, which includes variables created inside TPUStrategy scope, outside compilation logic must not include variable read/write. For variables placed on host, variable read/write is only allowed if the variable is not accessed by any other ops in the TPU computation. Variable read/write from outside compilation cluster is not visible from TPU computation and vice versa. Therefore, if outside compilation logic contains such host variables read/write ops and if the variables are accessed by TPU computation as well, then this may lead to deadlock.

Internally, `tf.tpu.outside_compilation()` adds outside compilation attributes to all ops in `computation`. During a later passes ops with outside compilation attributes are moved to a host-side graph. Inputs to this extract host-side graph are sent from TPU computation graph to host graph via a pair of XlaSendToHost and XlaRecvFromHost ops. Note that using `tf.tpu.outside_compilation()` may result in tensor transfer between TPU and CPU, leading to non-trivial performance impact.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `computation` | A Python function that builds the computation to place on the host. |
| `*args` | the positional arguments for the computation. |
| `**kwargs` | the keyword arguments for the computation. |

|     |
| --- |
| Returns<br>------- |     |
| The Tensors returned by computation. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.