[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/config/experimental/reset_memory_stats#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/config/experimental/reset_memory_stats)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/config/experimental/reset_memory_stats?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fconfig%2Fexperimental%2Freset_memory_stats&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/experimental/reset_memory_stats#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/config/experimental/reset_memory_stats#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.config.experimental.reset\_memory\_stats Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/experimental/reset_memory_stats#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/config/experimental/reset_memory_stats#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/config.py#L632-L670)

Resets the tracked memory stats for the chosen device.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.config.experimental.reset_memory_stats`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/reset_memory_stats)

tf.config.experimental.reset_memory_stats(
        device
    )

This function sets the tracked peak memory for a device to the device's current memory usage. This allows you to measure the peak memory usage for a specific part of your program. For example:

    if tf.config.list_physical_devices('GPU'):

Currently only supports GPU and TPU. If called on a CPU device, an exception will be raised.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `device` | Device string to reset the memory stats, e.g. `"GPU:0"`, `"TPU:0"`. See https://www.tensorflow.org/api\_docs/python/tf/device for specifying device strings. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | No device found with the device name, like '"nonexistent"'. |
| `ValueError` | Invalid device name, like '"GPU"', '"CPU:GPU"', '"CPU:"'. |
| `ValueError` | Multiple devices matched with the device name. |
| `ValueError` | Memory statistics not tracked or clearing memory statistics not supported, like '"CPU:0"'. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.