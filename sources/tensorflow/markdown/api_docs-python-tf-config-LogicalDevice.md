[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDevice#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDevice)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDevice?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fconfig%2FLogicalDevice&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Fields](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDevice#fields)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDevice#attributes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.config.LogicalDevice Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Fields](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDevice#fields)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDevice#attributes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/eager/context.py#L391-L406)

Abstraction for a logical device initialized by the runtime.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.config.LogicalDevice`](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDevice)

tf.config.LogicalDevice(
        name, device_type
    )

A [`tf.config.LogicalDevice`](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDevice)
 corresponds to an initialized logical device on a [`tf.config.PhysicalDevice`](https://www.tensorflow.org/api_docs/python/tf/config/PhysicalDevice)
 or a remote device visible to the cluster. Tensors and operations can be placed on a specific logical device by calling [`tf.device`](https://www.tensorflow.org/api_docs/python/tf/device)
 with a specified [`tf.config.LogicalDevice`](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDevice)
.

|     |     |
| --- | --- |
| Fields<br>------ |     |
| `name` | The fully qualified name of the device. Can be used for Op or function placement. |
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