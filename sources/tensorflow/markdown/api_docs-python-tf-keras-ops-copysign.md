[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/copysign#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/copysign)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/copysign?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/copysign#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/copysign#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.copysign Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/copysign#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/copysign#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/master/keras/src/ops/numpy.py#L2178-L2200)

Compose a value from the magnitude of `x1` and the sign of `x2`.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.copysign`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/copysign)

tf.keras.ops.copysign(
        x1, x2
    )

The sign of zero is taken into account, so an `x2` of `-0.0` gives a negative result and an `x2` of `0.0` gives a positive one.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x1` | Input tensor providing the magnitude. |
| `x2` | Input tensor providing the sign. |

|     |
| --- |
| Returns<br>------- |     |
| Output tensor with the magnitude of `x1` and the sign of `x2`. |     |

#### Example:

    x1 = keras.ops.convert_to_tensor([-1.0, 2.0, -3.0])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.