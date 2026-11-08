[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_info#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_info)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_info?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_info#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_info#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_info#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.config.experimental.get\_memory\_info Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_info#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_info#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_info#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/config.py#L583-L626)

Get memory info for the chosen device, as a dict.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.config.experimental.get_memory_info`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_info)

tf.config.experimental.get_memory_info(
        device
    )

This function returns a dict containing information about the device's memory usage. For example:

    if tf.config.list_physical_devices('GPU'):

Currently returns the following keys:

*   `'current'`: The current memory used by the device, in bytes.
*   `'peak'`: The peak memory used by the device across the run of the program, in bytes. Can be reset with [`tf.config.experimental.reset_memory_stats`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/reset_memory_stats)
    .

More keys may be added in the future, including device-specific keys.

Currently only supports GPU and TPU. If called on a CPU device, an exception will be raised.

For GPUs, TensorFlow will allocate all the memory by default, unless changed with [`tf.config.experimental.set_memory_growth`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_memory_growth)
. The dict specifies only the current and peak memory that TensorFlow is actually using, not the memory that TensorFlow has allocated on the GPU.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `device` | Device string to get the memory information for, e.g. `"GPU:0"`, `"TPU:0"`. See https://www.tensorflow.org/api\_docs/python/tf/device for specifying device strings. |

|     |
| --- |
| Returns<br>------- |     |
| A dict with keys `'current'` and `'peak'`, specifying the current and peak memory usage respectively. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | No device found with the device name, like '"nonexistent"'. |
| `ValueError` | Invalid device name, like '"GPU"', '"CPU:GPU"', '"CPU:"'. |
| `ValueError` | Multiple devices matched with the device name. |
| `ValueError` | Memory statistics not tracked, like '"CPU:0"'. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.