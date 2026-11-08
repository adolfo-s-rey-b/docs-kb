[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/debugging/set_log_device_placement#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/debugging/set_log_device_placement)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/debugging/set_log_device_placement?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdebugging%2Fset_log_device_placement&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/debugging/set_log_device_placement#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/debugging/set_log_device_placement#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.debugging.set\_log\_device\_placement Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/debugging/set_log_device_placement#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/debugging/set_log_device_placement#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/eager/context.py#L2812-L2844)

Turns logging for device placement decisions on or off.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.debugging.set_log_device_placement`](https://www.tensorflow.org/api_docs/python/tf/debugging/set_log_device_placement)

tf.debugging.set_log_device_placement(
        enabled
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Use a GPU](https://www.tensorflow.org/guide/gpu) |

Operations execute on a particular device, producing and consuming tensors on that device. This may change the performance of the operation or require TensorFlow to copy data to or from an accelerator, so knowing where operations execute is useful for debugging performance issues.

For more advanced profiling, use the [TensorFlow profiler](https://www.tensorflow.org/guide/profiler)
.

Device placement for operations is typically controlled by a [`tf.device`](https://www.tensorflow.org/api_docs/python/tf/device)
 scope, but there are exceptions, for example operations on a [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
 which follow the initial placement of the variable. Turning off soft device placement (with [`tf.config.set_soft_device_placement`](https://www.tensorflow.org/api_docs/python/tf/config/set_soft_device_placement)
) provides more explicit control.

    tf.debugging.set_log_device_placement(True)

Turning on [`tf.debugging.set_log_device_placement`](https://www.tensorflow.org/api_docs/python/tf/debugging/set_log_device_placement)
 also logs the placement of ops inside [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 when the function is called.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `enabled` | Whether to enabled device placement logging. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.