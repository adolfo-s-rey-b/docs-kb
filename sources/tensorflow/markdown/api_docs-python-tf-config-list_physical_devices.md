[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/config/list_physical_devices#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/config/list_physical_devices)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/config/list_physical_devices?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/config/list_physical_devices#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/list_physical_devices#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/config/list_physical_devices#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.config.list\_physical\_devices Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/config/list_physical_devices#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/list_physical_devices#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/config/list_physical_devices#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/config.py#L428-L470)

Return a list of physical devices visible to the host runtime.

#### View aliases

**Main aliases**

[`tf.config.experimental.list_physical_devices`](https://www.tensorflow.org/api_docs/python/tf/config/list_physical_devices)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.config.experimental.list_physical_devices`](https://www.tensorflow.org/api_docs/python/tf/config/list_physical_devices)
, [`tf.compat.v1.config.list_physical_devices`](https://www.tensorflow.org/api_docs/python/tf/config/list_physical_devices)

tf.config.list_physical_devices(
        device_type=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Use a GPU](https://www.tensorflow.org/guide/gpu)<br>    <br>*   [TensorFlow basics](https://www.tensorflow.org/guide/basics)<br>    <br>*   [Distributed training with Core APIs and DTensor](https://www.tensorflow.org/guide/core/distribution)<br>    <br>*   [Distributed training with TensorFlow](https://www.tensorflow.org/guide/distributed_training)<br>    <br>*   [DTensor concepts](https://www.tensorflow.org/guide/dtensor_overview) | *   [Customization basics: tensors and operations](https://www.tensorflow.org/tutorials/customization/basics)<br>    <br>*   [Custom layers](https://www.tensorflow.org/tutorials/customization/custom_layers)<br>    <br>*   [Using DTensors with Keras](https://www.tensorflow.org/tutorials/distribute/dtensor_keras_tutorial)<br>    <br>*   [Distributed training with DTensors](https://www.tensorflow.org/tutorials/distribute/dtensor_ml_tutorial)<br>    <br>*   [Distributed Input](https://www.tensorflow.org/tutorials/distribute/input) |

Physical devices are hardware devices present on the host machine. By default all discovered CPU and GPU devices are considered visible.

This API allows querying the physical hardware resources prior to runtime initialization. Thus, giving an opportunity to call any additional configuration APIs. This is in contrast to [`tf.config.list_logical_devices`](https://www.tensorflow.org/api_docs/python/tf/config/list_logical_devices)
, which triggers runtime initialization in order to list the configured devices.

The following example lists the number of visible GPUs on the host.

    physical_devices = tf.config.list_physical_devices('GPU')

However, the number of GPUs available to the runtime may change during runtime initialization due to marking certain devices as not visible or configuring multiple logical devices.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `device_type` | (optional string) Only include devices matching this device type. For example "CPU" or "GPU". |
| `Notes` | 1.  If provided with any numerical values or any string other than supported device type such as 'CPU' it returns an empty list instead of raising error. 2. For default value it returns all physical devices |

|     |
| --- |
| Returns<br>------- |     |
| List of discovered [`tf.config.PhysicalDevice`](https://www.tensorflow.org/api_docs/python/tf/config/PhysicalDevice)<br> objects |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.