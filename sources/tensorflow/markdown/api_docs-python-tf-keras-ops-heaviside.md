[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/heaviside#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/heaviside)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/heaviside?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/heaviside#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/heaviside#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.heaviside Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/heaviside#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/heaviside#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1488-L1510)

Heaviside step function.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.heaviside`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/heaviside)

tf.keras.ops.heaviside(
        x1, x2
    )

The Heaviside step function is defined as: `heaviside(x1, x2) = 0 if x1 < 0, 1 if x1 > 0, x2 if x1 == 0`

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x1` | A tensor input. |
| `x2` | A scalar or tensor, the value to return when `x1 == 0`. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor with a shape determined by broadcasting `x1` and `x2`. |     |

#### Example:

    x1 = keras.ops.convert_to_tensor([-2.0, 0.0, 3.0])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.