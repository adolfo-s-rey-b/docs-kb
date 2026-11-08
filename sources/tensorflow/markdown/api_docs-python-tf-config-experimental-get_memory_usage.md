[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_usage#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_usage)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_usage?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_usage#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_usage#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_usage#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.config.experimental.get\_memory\_usage Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_usage#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_usage#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_usage#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/config.py#L673-L709)

Get the current memory usage, in bytes, for the chosen device. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.config.experimental.get_memory_usage`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_usage)

tf.config.experimental.get_memory_usage(
        device
    )

This function is deprecated in favor of [`tf.config.experimental.get_memory_info`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_info)
. Calling this function is equivalent to calling `tf.config.experimental.get_memory_info()['current']`.

See [https://www.tensorflow.org/api\_docs/python/tf/device](https://www.tensorflow.org/api_docs/python/tf/device)
 for specifying device strings.

#### For example:

    gpu_devices = tf.config.list_physical_devices('GPU')

Does not work for CPU.

For GPUs, TensorFlow will allocate all the memory by default, unless changed with [`tf.config.experimental.set_memory_growth`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_memory_growth)
. This function only returns the memory that TensorFlow is actually using, not the memory that TensorFlow has allocated on the GPU.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `device` | Device string to get the bytes in use for, e.g. `"GPU:0"` |

|     |
| --- |
| Returns<br>------- |     |
| Total memory usage in bytes. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | Non-existent or CPU device specified. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.