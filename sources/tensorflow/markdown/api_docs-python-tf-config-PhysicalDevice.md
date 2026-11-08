[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/config/PhysicalDevice#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.config.PhysicalDevice Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/eager/context.py#L457-L481)

Abstraction for a locally visible physical device.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.config.PhysicalDevice`](https://www.tensorflow.org/api_docs/python/tf/config/PhysicalDevice)

tf.config.PhysicalDevice(
        name, device_type
    )

TensorFlow can utilize various devices such as the CPU or multiple GPUs for computation. Before initializing a local device for use, the user can customize certain properties of the device such as it's visibility or memory configuration.

Once a visible [`tf.config.PhysicalDevice`](https://www.tensorflow.org/api_docs/python/tf/config/PhysicalDevice)
 is initialized one or more [`tf.config.LogicalDevice`](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDevice)
 objects are created. Use [`tf.config.set_visible_devices`](https://www.tensorflow.org/api_docs/python/tf/config/set_visible_devices)
 to configure the visibility of a physical device and [`tf.config.set_logical_device_configuration`](https://www.tensorflow.org/api_docs/python/tf/config/set_logical_device_configuration)
 to configure multiple [`tf.config.LogicalDevice`](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDevice)
 objects for a [`tf.config.PhysicalDevice`](https://www.tensorflow.org/api_docs/python/tf/config/PhysicalDevice)
. This is useful when separation between models is needed or to simulate a multi-device environment.

|     |     |
| --- | --- |
| Fields<br>------ |     |
| `name` | Unique identifier for device. |
| `device_type` | String declaring the type of device such as "CPU" or "GPU". |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `name` | A `namedtuple` alias for field number 0 |
| `device_type` | A `namedtuple` alias for field number 1 |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.