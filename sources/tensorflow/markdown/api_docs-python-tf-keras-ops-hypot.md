[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hypot#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hypot)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hypot?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hypot#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hypot#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.hypot Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hypot#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hypot#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4083-L4111)

Element-wise hypotenuse of right triangles with legs `x1` and `x2`.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.hypot`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hypot)

tf.keras.ops.hypot(
        x1, x2
    )

This is equivalent to computing `sqrt(x1**2 + x2**2)` element-wise, with shape determined by broadcasting.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x1` | A tensor, representing the first leg of the right triangle. |
| `x2` | A tensor, representing the second leg of the right triangle. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor with a shape determined by broadcasting `x1` and `x2`. |     |

#### Example:

    x1 = keras.ops.convert_to_tensor([3.0, 4.0, 5.0])

    x1 = keras.ops.convert_to_tensor([[1, 2], [3, 4]])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.