[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/initialize_system#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/initialize_system)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/initialize_system?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/initialize_system#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/initialize_system#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.tpu.initialize\_system Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/initialize_system#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/initialize_system#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu.py#L82-L137)

Initializes a distributed TPU system for use with TensorFlow.

tf.compat.v1.tpu.initialize_system(
        embedding_config: Optional[embedding_pb2.TPUEmbeddingConfiguration] = None,
        job: Optional[Text] = None,
        compilation_failure_closes_chips: bool = True,
        tpu_cancellation_closes_chips: Optional[bool] = None
    ) -> core_types.Tensor

|     |     |
| --- | --- |
| Args<br>---- |     |
| `embedding_config` | If not None, a `TPUEmbeddingConfiguration` proto describing the desired configuration of the hardware embedding lookup tables. If embedding\_config is None, no hardware embeddings can be used. |
| `job` | The job (the XXX in TensorFlow device specification /job:XXX) that contains the TPU devices that will be initialized. If job=None it is assumed there is only one job in the TensorFlow flock, and an error will be returned if this assumption does not hold. |
| `compilation_failure_closes_chips` | Set the configuration whether we want to close TPU chips when there is a compilation failure. |
| `tpu_cancellation_closes_chips` | Set the configuration whether we want to close TPU chips when a TPU execution is cancelled. If the value is None, the behavior will be determined by the command line flag `tpu_cancellation_closes_chips` for the TPU worker. WARNING: this argument only applies to TFRT TPU runtime. |

|     |
| --- |
| Returns<br>------- |     |
| A serialized `TopologyProto` that describes the TPU system. Note: the topology must be evaluated using `Session.run` before it can be used. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.