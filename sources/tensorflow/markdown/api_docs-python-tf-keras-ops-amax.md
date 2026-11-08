[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/amax?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/amax)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/amax?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/amax?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/amax?version=stable#returns_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.amax Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/amax?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/amax?version=stable#returns_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L525-L559)

Returns the maximum of an array or maximum value along an axis.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.amax`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/amax)

tf.keras.ops.amax(
        x, axis=None, keepdims=False
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |
| `axis` | Axis along which to compute the maximum. By default (`axis=None`), find the maximum value in all the dimensions of the input array. |
| `keepdims` | If `True`, axes which are reduced are left in the result as dimensions that are broadcast to the size of the original input tensor. Defaults to `False`. |

|     |
| --- |
| Returns<br>------- |     |
| An array with the maximum value. If `axis=None`, the result is a scalar value representing the maximum element in the entire array. If `axis` is given, the result is an array with the maximum values along the specified axis. |     |

#### Examples:

    x = keras.ops.convert_to_tensor([[1, 3, 5], [2, 3, 6]])

    x = keras.ops.convert_to_tensor([[1, 6, 8], [1, 5, 2]])

    x = keras.ops.convert_to_tensor([[1, 6, 8], [1, 5, 2]])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-04 UTC.