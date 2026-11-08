[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/TPUSystemMetadata#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/TPUSystemMetadata)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/TPUSystemMetadata?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/TPUSystemMetadata#attributes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.tpu.experimental.TPUSystemMetadata Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/TPUSystemMetadata#attributes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_system_metadata.py#L40-L65)

Describes some metadata about the TPU system.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.tpu.experimental.TPUSystemMetadata`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/TPUSystemMetadata)

tf.tpu.experimental.TPUSystemMetadata(
        num_cores, num_hosts, num_of_cores_per_host, topology, devices
    )

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `num_cores` | interger. Total number of TPU cores in the TPU system. |
| `num_hosts` | interger. Total number of hosts (TPU workers) in the TPU system. |
| `num_of_cores_per_host` | interger. Number of TPU cores per host (TPU worker). |
| `topology` | an instance of [`tf.tpu.experimental.Topology`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/Topology)<br>, which describes the physical topology of TPU system. |
| `devices` | a tuple of strings, which describes all the TPU devices in the system. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.