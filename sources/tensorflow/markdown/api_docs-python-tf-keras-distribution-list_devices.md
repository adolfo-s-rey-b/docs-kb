[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/list_devices#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/list_devices)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/list_devices?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/list_devices#args)
    
*   [Return](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/list_devices#return)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.distribution.list\_devices Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/list_devices#args)
    
*   [Return](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/list_devices#return)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distribution/distribution_lib.py#L21-L42)

Return all the available devices based on the device type.

tf.keras.distribution.list_devices(
        device_type=None
    )

When `device_type` is not provided, devices of the default type are returned. This function nevers return a mix of device types, for instance GPUs and CPUs.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `device_type` | string, one of `"cpu"`, `"gpu"` or `"tpu"`. Defaults to `"gpu"` or `"tpu"` if available when `device_type` is not provided. Otherwise returns the `"cpu"` devices. |

|     |
| --- |
| Return<br>------ |     |
| List of string, the devices that are available for distributed computation. Each device is formatted as "device\_type:id", for instance "gpu:1" or "cpu:0". |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.