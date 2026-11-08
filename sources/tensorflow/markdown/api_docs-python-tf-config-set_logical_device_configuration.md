[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/config/set_logical_device_configuration#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/config/set_logical_device_configuration)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/config/set_logical_device_configuration?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/config/set_logical_device_configuration#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/set_logical_device_configuration#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/config/set_logical_device_configuration#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.config.set\_logical\_device\_configuration Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/config/set_logical_device_configuration#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/set_logical_device_configuration#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/config/set_logical_device_configuration#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/config.py#L855-L924)

Set the logical device configuration for a [`tf.config.PhysicalDevice`](https://www.tensorflow.org/api_docs/python/tf/config/PhysicalDevice)
.

#### View aliases

**Main aliases**

[`tf.config.experimental.set_virtual_device_configuration`](https://www.tensorflow.org/api_docs/python/tf/config/set_logical_device_configuration)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.config.experimental.set_virtual_device_configuration`](https://www.tensorflow.org/api_docs/python/tf/config/set_logical_device_configuration)
, [`tf.compat.v1.config.set_logical_device_configuration`](https://www.tensorflow.org/api_docs/python/tf/config/set_logical_device_configuration)

tf.config.set_logical_device_configuration(
        device, logical_devices
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Use a GPU](https://www.tensorflow.org/guide/gpu)<br>    <br>*   [Distributed training with Core APIs and DTensor](https://www.tensorflow.org/guide/core/distribution)<br>    <br>*   [DTensor concepts](https://www.tensorflow.org/guide/dtensor_overview)<br>    <br>*   [Random number generation](https://www.tensorflow.org/guide/random_numbers) | *   [Using DTensors with Keras](https://www.tensorflow.org/tutorials/distribute/dtensor_keras_tutorial)<br>    <br>*   [Distributed training with DTensors](https://www.tensorflow.org/tutorials/distribute/dtensor_ml_tutorial)<br>    <br>*   [Distributed Input](https://www.tensorflow.org/tutorials/distribute/input)<br>    <br>*   [TFF simulations with accelerators](https://www.tensorflow.org/federated/tutorials/simulations_with_accelerators)<br>    <br>*   [TFP Release Notes notebook (0.12.1)](https://www.tensorflow.org/probability/examples/TFP_Release_Notebook_0_12_1) |

A visible [`tf.config.PhysicalDevice`](https://www.tensorflow.org/api_docs/python/tf/config/PhysicalDevice)
 will by default have a single [`tf.config.LogicalDevice`](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDevice)
 associated with it once the runtime is initialized. Specifying a list of [`tf.config.LogicalDeviceConfiguration`](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDeviceConfiguration)
 objects allows multiple devices to be created on the same [`tf.config.PhysicalDevice`](https://www.tensorflow.org/api_docs/python/tf/config/PhysicalDevice)
.

Logical device configurations can be modified by calling this function as long as the runtime is uninitialized. After the runtime is initialized calling this function raises a RuntimeError.

The following example splits the CPU into 2 logical devices:

    physical_devices = tf.config.list_physical_devices('CPU')

The following example splits the GPU into 2 logical devices with 100 MB each:

    physical_devices = tf.config.list_physical_devices('GPU')

|     |     |
| --- | --- |
| Args<br>---- |     |
| `device` | The `PhysicalDevice` to configure. |
| `logical_devices` | (optional) List of [`tf.config.LogicalDeviceConfiguration`](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDeviceConfiguration)<br> objects to allocate for the specified `PhysicalDevice`. If None, the default configuration will be used. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If argument validation fails. |
| `RuntimeError` | Runtime is already initialized. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.