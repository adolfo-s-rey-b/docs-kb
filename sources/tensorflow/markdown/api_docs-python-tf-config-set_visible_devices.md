[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/config/set_visible_devices#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/config/set_visible_devices)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/config/set_visible_devices?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/config/set_visible_devices#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/set_visible_devices#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/config/set_visible_devices#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.config.set\_visible\_devices Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/config/set_visible_devices#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/set_visible_devices#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/config/set_visible_devices#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/config.py#L545-L578)

Set the list of visible devices.

#### View aliases

**Main aliases**

[`tf.config.experimental.set_visible_devices`](https://www.tensorflow.org/api_docs/python/tf/config/set_visible_devices)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.config.experimental.set_visible_devices`](https://www.tensorflow.org/api_docs/python/tf/config/set_visible_devices)
, [`tf.compat.v1.config.set_visible_devices`](https://www.tensorflow.org/api_docs/python/tf/config/set_visible_devices)

tf.config.set_visible_devices(
        devices, device_type=None
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Use a GPU](https://www.tensorflow.org/guide/gpu) |

Specifies which `PhysicalDevice` objects are visible to the runtime. TensorFlow will only allocate memory and place operations on visible physical devices, as otherwise no `LogicalDevice` will be created on them. By default all discovered devices are marked as visible.

The following example demonstrates disabling the first GPU on the machine.

    physical_devices = tf.config.list_physical_devices('GPU')

|     |     |
| --- | --- |
| Args<br>---- |     |
| `devices` | List of `PhysicalDevice`s to make visible |
| `device_type` | (optional) Only configure devices matching this device type. For example "CPU" or "GPU". Other devices will be left unaltered. |

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