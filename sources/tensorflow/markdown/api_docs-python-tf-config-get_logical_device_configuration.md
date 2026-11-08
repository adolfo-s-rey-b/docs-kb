[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/config/get_logical_device_configuration#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/config/get_logical_device_configuration)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/config/get_logical_device_configuration?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/get_logical_device_configuration#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/config/get_logical_device_configuration#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.config.get\_logical\_device\_configuration Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/get_logical_device_configuration#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/config/get_logical_device_configuration#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/config.py#L814-L852)

Get the virtual device configuration for a [`tf.config.PhysicalDevice`](https://www.tensorflow.org/api_docs/python/tf/config/PhysicalDevice)
.

#### View aliases

**Main aliases**

[`tf.config.experimental.get_virtual_device_configuration`](https://www.tensorflow.org/api_docs/python/tf/config/get_logical_device_configuration)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.config.experimental.get_virtual_device_configuration`](https://www.tensorflow.org/api_docs/python/tf/config/get_logical_device_configuration)
, [`tf.compat.v1.config.get_logical_device_configuration`](https://www.tensorflow.org/api_docs/python/tf/config/get_logical_device_configuration)

tf.config.get_logical_device_configuration(
        device
    )

Returns the list of [`tf.config.LogicalDeviceConfiguration`](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDeviceConfiguration)
 objects previously configured by a call to [`tf.config.set_logical_device_configuration`](https://www.tensorflow.org/api_docs/python/tf/config/set_logical_device_configuration)
.

#### For example:

    physical_devices = tf.config.list_physical_devices('CPU')

|     |     |
| --- | --- |
| Args<br>---- |     |
| `device` | `PhysicalDevice` to query |

|     |
| --- |
| Returns<br>------- |     |
| List of [`tf.config.LogicalDeviceConfiguration`](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDeviceConfiguration)<br> objects or `None` if no virtual device configuration has been set for this physical device. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.