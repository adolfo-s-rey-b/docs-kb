[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_device_policy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_device_policy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_device_policy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fconfig%2Fexperimental%2Fset_device_policy&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_device_policy#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_device_policy#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.config.experimental.set\_device\_policy Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_device_policy#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_device_policy#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/config.py#L344-L387)

Sets the current thread device policy.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.config.experimental.set_device_policy`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_device_policy)

tf.config.experimental.set_device_policy(
        device_policy
    )

The device policy controls how operations requiring inputs on a specific device (e.g., on GPU:0) handle inputs on a different device (e.g. GPU:1).

When using the default, an appropriate policy will be picked automatically. The default policy may change over time.

This function only sets the device policy for the current thread. Any subsequently started thread will again use the default policy.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `device_policy` | A device policy. Valid values:<br><br>*   None: Switch to a system default.<br>*   'warn': Copies the tensors which are not on the right device and logs a warning.<br>*   'explicit': Raises an error if the placement is not as required.<br>*   'silent': Silently copies the tensors. Note that this may hide performance problems as there is no notification provided when operations are blocked on the tensor being copied between devices.<br>*   'silent\_for\_int32': silently copies `int32` tensors, raising errors on the other ones. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If an invalid `device_policy` is passed. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.