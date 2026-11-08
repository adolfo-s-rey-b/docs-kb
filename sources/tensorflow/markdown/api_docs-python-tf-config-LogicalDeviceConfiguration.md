[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDeviceConfiguration#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDeviceConfiguration)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDeviceConfiguration?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDeviceConfiguration#used-in-the-notebooks)
    
*   [Fields](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDeviceConfiguration#fields)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDeviceConfiguration#attributes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.config.LogicalDeviceConfiguration Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDeviceConfiguration#used-in-the-notebooks)
    
*   [Fields](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDeviceConfiguration#fields)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDeviceConfiguration#attributes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/eager/context.py#L409-L454)

Configuration class for a logical devices.

#### View aliases

**Main aliases**

[`tf.config.experimental.VirtualDeviceConfiguration`](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDeviceConfiguration)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.config.LogicalDeviceConfiguration`](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDeviceConfiguration)
, [`tf.compat.v1.config.experimental.VirtualDeviceConfiguration`](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDeviceConfiguration)

tf.config.LogicalDeviceConfiguration(
        memory_limit=None,
        experimental_priority=None,
        experimental_device_ordinal=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Use a GPU](https://www.tensorflow.org/guide/gpu)<br>    <br>*   [Random number generation](https://www.tensorflow.org/guide/random_numbers)<br>    <br>*   [Distributed training with Core APIs and DTensor](https://www.tensorflow.org/guide/core/distribution)<br>    <br>*   [DTensor concepts](https://www.tensorflow.org/guide/dtensor_overview) | *   [Using DTensors with Keras](https://www.tensorflow.org/tutorials/distribute/dtensor_keras_tutorial)<br>    <br>*   [Distributed training with DTensors](https://www.tensorflow.org/tutorials/distribute/dtensor_ml_tutorial)<br>    <br>*   [Distributed Input](https://www.tensorflow.org/tutorials/distribute/input)<br>    <br>*   [TFF simulations with accelerators](https://www.tensorflow.org/federated/tutorials/simulations_with_accelerators)<br>    <br>*   [TFP Release Notes notebook (0.12.1)](https://www.tensorflow.org/probability/examples/TFP_Release_Notebook_0_12_1) |

The class specifies the parameters to configure a [`tf.config.PhysicalDevice`](https://www.tensorflow.org/api_docs/python/tf/config/PhysicalDevice)
 as it is initialized to a [`tf.config.LogicalDevice`](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDevice)
 during runtime initialization. Not all fields are valid for all device types.

See [`tf.config.get_logical_device_configuration`](https://www.tensorflow.org/api_docs/python/tf/config/get_logical_device_configuration)
 and [`tf.config.set_logical_device_configuration`](https://www.tensorflow.org/api_docs/python/tf/config/set_logical_device_configuration)
 for usage examples.

|     |     |
| --- | --- |
| Fields<br>------ |     |
| `memory_limit` | (optional) Maximum memory (in MB) to allocate on the virtual device. Currently only supported for GPUs. |
| `experimental_priority` | (optional) Priority to assign to a virtual device. Lower values have higher priorities and 0 is the default. Within a physical GPU, the GPU scheduler will prioritize ops on virtual devices with higher priority. Currently only supported for Nvidia GPUs. |
| `experimental_device_ordinal` | (optional) Ordinal number to order the virtual device. LogicalDevice with lower ordinal number will receive a lower device id. Physical device id and location in the list is used to break ties. Currently only supported for Nvidia GPUs. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `memory_limit` | A `namedtuple` alias for field number 0 |
| `experimental_priority` | A `namedtuple` alias for field number 1 |
| `experimental_device_ordinal` | A `namedtuple` alias for field number 2 |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.