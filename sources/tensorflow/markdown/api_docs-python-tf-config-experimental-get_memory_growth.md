[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_growth#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_growth)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_growth?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fconfig%2Fexperimental%2Fget_memory_growth&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_growth#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_growth#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_growth#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.config.experimental.get\_memory\_growth Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_growth#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_growth#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_growth#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/config.py#L712-L738)

Get if memory growth is enabled for a `PhysicalDevice`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.config.experimental.get_memory_growth`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_growth)

tf.config.experimental.get_memory_growth(
        device
    )

If memory growth is enabled for a `PhysicalDevice`, the runtime initialization will not allocate all memory on the device.

#### For example:

    physical_devices = tf.config.list_physical_devices('GPU')

|     |     |
| --- | --- |
| Args<br>---- |     |
| `device` | `PhysicalDevice` to query |

|     |
| --- |
| Returns<br>------- |     |
| A boolean indicating the memory growth setting for the `PhysicalDevice`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | Invalid `PhysicalDevice` specified. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.