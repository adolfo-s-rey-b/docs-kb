[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_device_details#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_device_details)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_device_details?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fconfig%2Fexperimental%2Fget_device_details&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_device_details#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_device_details#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.config.experimental.get\_device\_details Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_device_details#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_device_details#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/config.py#L769-L811)

Returns details about a physical devices.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.config.experimental.get_device_details`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_device_details)

tf.config.experimental.get_device_details(
        device
    )

This API takes in a [`tf.config.PhysicalDevice`](https://www.tensorflow.org/api_docs/python/tf/config/PhysicalDevice)
 returned by [`tf.config.list_physical_devices`](https://www.tensorflow.org/api_docs/python/tf/config/list_physical_devices)
. It returns a dict with string keys containing various details about the device. Each key is only supported by a subset of devices, so you should not assume the returned dict will have any particular key.

    gpu_devices = tf.config.list_physical_devices('GPU')

Currently, details are only returned for GPUs. This function returns an empty dict if passed a non-GPU device.

The returned dict may have the following keys:

*   `'device_name'`: A human-readable name of the device as a string, e.g. "Titan V". Unlike [`tf.config.PhysicalDevice.name`](https://www.tensorflow.org/api_docs/python/tf/config/PhysicalDevice#name)
    , this will be the same for multiple devices if each device is the same model. Currently only available for GPUs.
*   `'compute_capability'`: The [compute capability](https://developer.nvidia.com/cuda-gpus)
     of the device as a tuple of two ints, in the form `(major_version, minor_version)`. Only available for NVIDIA GPUs

|     |     |
| --- | --- |
| Args<br>---- |     |
| `device` | A [`tf.config.PhysicalDevice`](https://www.tensorflow.org/api_docs/python/tf/config/PhysicalDevice)<br> returned by [`tf.config.list_physical_devices`](https://www.tensorflow.org/api_docs/python/tf/config/list_physical_devices)<br> or [`tf.config.get_visible_devices`](https://www.tensorflow.org/api_docs/python/tf/config/get_visible_devices)<br>. |

|     |
| --- |
| Returns<br>------- |     |
| A dict with string keys. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.