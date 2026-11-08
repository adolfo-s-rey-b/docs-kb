[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/shutdown_tpu_system#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/shutdown_tpu_system)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/shutdown_tpu_system?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Ftpu%2Fexperimental%2Fshutdown_tpu_system&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/shutdown_tpu_system#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/shutdown_tpu_system#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.tpu.experimental.shutdown\_tpu\_system Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/shutdown_tpu_system#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/shutdown_tpu_system#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver.py#L76-L92)

Shuts down the TPU devices.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.tpu.experimental.shutdown_tpu_system`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/shutdown_tpu_system)

tf.tpu.experimental.shutdown_tpu_system(
        cluster_resolver=None
    )

This will clear all caches, even those that are maintained through sequential calls to tf.tpu.experimental.initialize\_tpu\_system, such as the compilation cache.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `cluster_resolver` | A tf.distribute.cluster\_resolver.TPUClusterResolver, which provides information about the TPU cluster. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `RuntimeError` | If no TPU devices found for eager execution or if run in a tf.function. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.