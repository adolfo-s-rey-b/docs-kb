[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/get_device_count#main-content)

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
    

tf.keras.distribution.get\_device\_count Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distribution/distribution_lib.py#L45-L61)

Returns the number of available devices based on the device type.

tf.keras.distribution.get_device_count(
        device_type=None
    )

When `device_type` is not provided, the count of devices of the default type is returned. This function nevers counts a mix of device types, for instance GPUs and CPUs.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `device_type` | string, one of `"cpu"`, `"gpu"` or `"tpu"`. Defaults to `"gpu"` or `"tpu"` if available when `device_type` is not provided. Otherwise returns the `"cpu"` devices. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `int` | The total number of devices for the specified type. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.