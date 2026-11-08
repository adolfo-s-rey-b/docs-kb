[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/angle#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/angle)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/angle?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/keras/ops/angle#arguments)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/angle#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.angle Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/keras/ops/angle#arguments)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/angle#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L417-L436)

Element-wise angle of a complex tensor.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.angle`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/angle)

tf.keras.ops.angle(
        x
    )

|     |     |
| --- | --- |
| Arguments<br>--------- |     |
| `x` | Input tensor. Can be real or complex. |

|     |
| --- |
| Returns<br>------- |     |
| Output tensor of same shape as x. containing the angle of each element (in radians). |     |

#### Example:

    x = keras.ops.convert_to_tensor([[1 + 3j, 2 - 5j], [4 - 3j, 3 + 2j]])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.